package edenEquips;

use strict;
use warnings;
use Plugins;
use Log qw(message warning error);
use Commands;
use Settings;
use File::Spec;
use File::Basename qw(dirname);
use Cwd qw(getcwd abs_path);
use Encode qw(decode);
use Globals qw($char);
use Time::HiRes qw(time);

Plugins::register('edenEquips', \&onUnload);

my $plugin_dir  = dirname(abs_path(__FILE__));
my $supabase_url = "https://bnjjwtbjanjkledoiwem.supabase.co";
my $anon_key     = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJuamp3dGJqYW5qa2xlZG9pd2VtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjAxOTk4MzAsImV4cCI6MjA3NTc3NTgzMH0.N3wNjGbKM8QCZ2v3EbXksgawmwdG5Vo1AxQUE_81K10"; # ajuste se necessário
my $python_cmd   = "python3";
my $injection_done;
my $injection_in_progress;
my $auth_status  = 'unknown';
my $check_interval = 3600; # seconds
my $next_check_time;

Plugins::addHooks(
    ['in_game', \&maybe_inject_macros],
    ['mainLoop_post', \&periodic_authorization_check],
);

maybe_inject_macros();

sub maybe_inject_macros {
    return if $injection_done || $injection_in_progress;
    return unless $char && $char->{charID};

    my ($macro_file, $macro_display) = resolve_macro_destination();

    unless (-e $macro_file) {
        warning "[edenEquips] File $macro_file not found. Aborting.\n";
        return;
    }

    $injection_in_progress = 1;

    message "Carregando $macro_display..\n";

    if (update_proxy_and_inject($macro_file)) {
        $injection_done = 1;
        $auth_status    = 'allowed';
        schedule_next_check();
    }

    $injection_in_progress = 0;
}

sub schedule_next_check {
    $next_check_time = time + $check_interval;
}

sub resolve_macro_destination {
    my $control_dir;

    if (my $config_path = eval { Settings::getControlFilename("config.txt") }) {
        $control_dir = dirname($config_path) if $config_path;
    }

    unless ($control_dir) {
        $control_dir = File::Spec->catdir(getcwd(), "control");
    }

    my $macro_file = File::Spec->catfile($control_dir, "eventMacros.txt");
    my $macro_display = eval { File::Spec->abs2rel($macro_file, getcwd()) } || $macro_file;

    return ($macro_file, $macro_display);
}

sub update_proxy_and_inject {
    my ($macro_file) = @_;
    my ($res, $decoded) = fetch_macro_payload();

    return 0 if $res != 0;

    if ($decoded !~ /automacro|timeout|call\s*\{/) {
        warning "[edenEquips] Doesn't look like eventMmacro — aborting. Preview: "
            . substr($decoded,0,200) . "\n";
        return 0;
    }

    unless (-e $macro_file) {
        warning "[edenEquips] File $macro_file not found. Aborting.\n";
        return 0;
    }

    my $original = "";
    if (open my $mf, "<", $macro_file) { local $/; $original = <$mf>; close $mf; }

    if (open my $out, ">", $macro_file) {
        print $out $original;
        print $out "\n\n# --- [edenEquips] NÃO DELETE ---\n";
        print $out $decoded;
        close $out;
    } else {
        warning "[edenEquips] Failed to write $macro_file\n";
        return 0;
    }

    Commands::run("reload eventMacros");

    if (open my $rf, ">", $macro_file) {
        print $rf $original;
        close $rf;
    } else {
        warning "[edenEquips] Failed to restore $macro_file\n";
    }

    return 1;
}

sub onUnload {
    message "[edenEquips] Plugin unloaded.\n";
}

sub fetch_macro_payload {
    my ($quiet) = @_;
    my $py_script = File::Spec->catfile($plugin_dir, "proxy.py");
    my $cmd = qq("$python_cmd" "$py_script" "$supabase_url" "$anon_key");

    message "[edenEquips] Running (stdout) ...\n" unless $quiet;

    my $output = `$cmd 2>&1`;
    my $res = $? >> 8;

    $output = eval { decode("UTF-8", $output) } || $output;

    if ($res != 0) {
        unless ($quiet) {
            warning "[edenEquips] HWID access denied. stderr:\n$output\n";
            warning "[edenEquips] Contact and send HWID for activation.";
            warning "[DISCORD] https://discord.com/users/boscv.";
        }
        return ($res, undef);
    }

    return (0, $output);
}

sub periodic_authorization_check {
    return unless $char && $char->{charID};

    my $now = time;
    if (!$next_check_time) {
        schedule_next_check();
        return;
    }

    return if $now < $next_check_time;

    schedule_next_check();

    message "[edenEquips] Executando verificação periódica de HWID...\n";

    my ($res, undef) = fetch_macro_payload(1);

    if ($res != 0) {
        if ($auth_status ne 'denied') {
            warning "[edenEquips] HWID access revoked. Reloading eventMacros.\n";
        }
        if ($injection_done) {
            Commands::run("reload eventMacros");
        }
        $injection_in_progress = 0;
        $injection_done        = 0;
        $auth_status           = 'denied';
        return;
    }

    if ($auth_status eq 'denied') {
        message "[edenEquips] HWID access restored. Reapplying macros if needed.\n";
    }

    $auth_status = 'allowed';

    maybe_inject_macros() unless $injection_done;
}

1;
