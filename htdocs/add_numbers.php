<!DOCTYPE html>
<html>
<head>
    <title>Result</title>
</head>
<body>
    <h1>Addition Result</h1>

    <?php
        if (isset($_GET['num1']) && isset($_GET['num2']))
            echo $_GET['num1'] + $_GET['num2'];
        else
            echo "empty";
    ?>

</body>
</html>
