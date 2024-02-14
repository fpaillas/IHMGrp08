<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8">
    <title>EVENT'O Page d'accueil</title>
    <link rel="stylesheet" type="text/css" href="../main/main.css"/>
  </head>
  <body>
    <!----------------- entête haut de page ----------------->
    <iframe src="../header/header.html" width="100%" height="180vw" frameborder="0"></iframe>
    <iframe src="../menub/menu.html" width="100%" frameborder="0" ></iframe>
    <!----------------- Suggestion du moment (début)----------------->
    <div class="cadre">
      <p>"Suggestion du moment"</p>
      <!----------------- Péparation requete (début)----------------->
      <!-- <?php
        // Inclusion du fichier de connexion à la BDD
        include("../connexion_bdd.php");
        
        //session_start(); // initialisation de la session
        include("../time_session.php");

        // Requête SQL pour récupérer les données de la table Produit et Service
        $sql = "SELECT * FROM Produit WHERE Suggestion = 1"; //Produit suggérer
        $sqls = "SELECT * FROM Service WHERE Suggestion = 1"; // Service suggérer
        $sqlt = "SELECT * FROM Produit"; // Pour affichage produit
        $sqlst = "SELECT * FROM Service"; // Pour affichage service
   
        // Exécuter la requête SQL
        $stmt = $bdd->query($sql);
        $stmts = $bdd->query($sqls);
        $stmtt = $bdd->query($sqlt);
        $stmtst = $bdd->query($sqlst);
      ?> -->
      <!----------------- Péparation requete (fin)----------------->
      <!----------------- Affichage suggestion du moment (début)----------------->
      <div class="listing">
        <?php foreach ($stmt as $row) : ?>
          <form action="../product(fiche)/product.php" method="GET">
            <input type="hidden" name="idProduit" value="<?php echo $row['idProduit']; ?>">
            <div class="ajustement">
              <p>
              <button type="submit" name="submit">
                <img src="..//img/img_prod/<?= $row["idProduit"] ?>.jpg" width="80" height="80" alt="Image du produit">
              </button>
              <br>
              <?php echo $row["NomP"] ?> <br>
              <?= $row["Prix"] ?> €</p> <br>
            </div>
          </form>
        <?php endforeach; ?>
        <?php foreach ($stmts as $row) : ?>
          <form action="../service(fiche)/service.php" method="GET">
            <input type="hidden" name="idService" value="<?php echo $row['idService']; ?>">
            <div class="ajustement">
              <p>
              <button type="submit" name="submit">
                <img src="../img/testballon.jpg" width="80" height="80" alt="Ballon NB">
              </button>
              <br>
              <?php echo $row["NomS"] ?> <br> 
              <?php echo $row["NomC"] . ' ' . $row["PrenomC"] ?> <br>
              <?php echo $row["CategorieS"] ?> </p>
            </div>
          </form>
        <?php endforeach; ?>
      </div>
    </div>
    <!----------------- Affichage suggestion du moment (fin)----------------->
    <br>
    <!----------------- Affichage de produit et service (début)----------------->
    <div class="tout">  
      <h1>Pates</h1>   <br>
      <img src="..//img/testballon"> <br>
      <p>Details de préparation</p> <br>
      <!-- <?php foreach ($stmtt as $row) : ?>
        <form action="../product(fiche)/product.php" method="GET">
          <input type="hidden" name="idProduit" value="<?php echo $row['idProduit']; ?>">
          <div class="ajuster">
            <p>
            <button type="submit" name="submit">
            <img src="..//img/img_prod/<?= $row["idProduit"] ?>.jpg" width="80" height="80" alt="Image du produit">
            </button>
            <br>
            <?php echo $row["NomP"] ?> <br>
            <?= $row["Prix"] ?> €</p> <br>
          </div>
        </form>
      <?php endforeach; ?>    -->   
    </div>
    <!----------------- Affichage de produit et service (fin)------------------->

  </body>
</html>
