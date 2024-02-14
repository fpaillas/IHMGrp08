<!----------------- Page test pour la suggestion----------------->
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" href="../main/main.css"/>
  </head>
  <body>
    <?php
      // Inclusion du fichier de connexion à la BDD
      include("../connexion_bdd.php");

      //session_start(); // initialisation de la session
      include("../time_session.php");
      
      // Requête SQL pour récupérer les données de la table Produit et Service
      $sql = "SELECT * FROM Produit WHERE Suggestion = 1";
      $sqls = "SELECT * FROM Service WHERE Suggestion = 1";
    
      // Exécuter la requête SQL
      $stmt = $bdd->query($sql);
      $stmts = $bdd->query($sqls);
    ?>
  <div>
  <?php foreach ($stmt as $row) : ?>
    <li><?php echo $row["NomP"] ?></li> 
    <li><?php echo $row["NomP"] ?></li>
    <li><?= $row["Prix"] ?> €</li>
  <?php endforeach; ?>
  <?php foreach ($stmts as $row) : ?>
    <li><?php echo $row["NomS"] ?></li> 
    <li><?php echo $row["NomC"] . ' ' . $row["PrenomC"] ?></li>
    <li><?php echo $row["CategorieS"] ?> </li>
  <?php endforeach; ?>
  </div>
  </body>
</html>
