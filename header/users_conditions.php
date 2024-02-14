<!------------ Condition de redirection selon l'état de connexion et individu (début) --------->
<?php
//Inclusion du fichier de connexion à la BDD
include("../connexion_bdd.php");

//session_start(); // initialisation de la session
include("../time_session.php");

if ($_SERVER['REQUEST_METHOD'] == 'GET') {
    if(isset($_SESSION['idUtilisateur'])){ // Vérifier si une session utilisateur existe
        if($_SESSION['idUtilisateur'] == 1){ // Vérifier si l'utilisateur est un admin (id=1)
            header('Location: ../admin/admin.html'); // Rediriger vers la page admin.php
            exit(); // Arrêter le script pour éviter toute exécution supplémentaire
        } else {
            header('Location: ../perso/perso.html'); // Rediriger vers la page perso.php = tableau de bord d'un utilisateur
            exit(); // Arrêter le script pour éviter toute exécution supplémentaire
        }
    } else {
        header('Location: ../connexion/connexion.html'); // Rediriger vers la page connexion.html
        exit(); // Arrêter le script pour éviter toute exécution supplémentaire
    }
}
?>
<!------------ Condition de redirection selon l'état de connexion et individu (fin) --------->
