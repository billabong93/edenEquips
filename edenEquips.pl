package edenEquips;

use strict;
use warnings;
use Plugins;
use Log qw(message warning error);
use Commands;
use Time::HiRes qw(time);
use File::Spec;
use Cwd qw(getcwd abs_path);
use Encode qw(decode);

Plugins::register('edenEquips', \&onUnload);

my $plugin_dir  = abs_path("plugins/edenEquips");
my $control_dir = File::Spec->catdir(getcwd(), "control");
my $macro_file  = File::Spec->catfile($control_dir, "eventMacros.txt");

my $supabase_url = "https://bnjjwtbjanjkledoiwem.supabase.co";
my $anon_key     = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJuamp3dGJqYW5qa2xlZG9pd2VtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjAxOTk4MzAsImV4cCI6MjA3NTc3NTgzMH0.N3wNjGbKM8QCZ2v3EbXksgawmwdG5Vo1AxQUE_81K10"; # ajuste se necessário
my $python_cmd   = "python3";

update_proxy_and_inject();

sub update_proxy_and_inject {
    my $py_script = File::Spec->catfile($plugin_dir, "proxy.py");
    my $cmd = qq("$python_cmd" "$py_script" "$supabase_url" "$anon_key");

    message "[edenEquips] Running (stdout) ...\n";
    my $output = `$cmd 2>&1`;
    my $res = $? >> 8;

    $output = eval { decode("UTF-8", $output) } || $output;

    if ($res != 0) {
        warning "[edenEquips] HWID access denied. stderr:\n$output\n";
        warning "[edenEquips] Contact and send HWID for registration.";
        warning "[DISCORD] https://discord.com/users/boscv.";
        return;
    }

    my $decoded = $output;

    if ($decoded !~ /automacro|timeout|call\s*\{/) {
        warning "[edenEquips] Conteúdo recebido parece  — abortando. Preview: "
            . substr($decoded,0,200) . "\n";
        return;
    }

    unless (-e $macro_file) {
        warning "[edenEquips] Arquivo $macro_file não encontrado. Abortando.\n";
        return;
    }

    my $original = "";
    if (open my $mf, "<", $macro_file) { local $/; $original = <$mf>; close $mf; }

    if (open my $out, ">", $macro_file) {
        print $out $original;
        print $out "\n\n# --- [edenEquips] Não delete ---\n";
        print $out $decoded;
        close $out;
    } else {
        warning "[edenEquips] Falha ao escrever $macro_file\n";
        return;
    }

    Commands::run("reload eventMacros");

    if (open my $rf, ">", $macro_file) {
        print $rf $original;
        close $rf;
    } else {
        warning "[edenEquips] Falha ao restaurar $macro_file\n";
    }

}

sub onUnload {
    message "[edenEquips] Plugin descarregado.\n";
}

1;
