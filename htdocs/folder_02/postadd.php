<html>
    <body>
<?php

if (isset($_POST['n1']) && isset($_POST['n2']))
    echo $_POST['n1'] + $_POST['n2'];
else
    echo "empty";



?>
<!--if (isset($_POST['n1']) && isset($_POST['n2']))
    echo $_POST['n1'] + $_POST['n2'];-->
</body>
</html>