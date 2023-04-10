<?php

echo "Welcome";
if(isset($_POST['pnumber']))
{
    echo "HII";
    $_SERVER="localhost";
    $username="root";
    $password="";
    $database="hridoy";
    $connect=mysqli_connect($_SERVER,$username,$password,$database);

    if(!$connect)
    {
       die(mysqli_connect_error());
    }
    echo "<br>";
    echo "Connected";
}

$name=$_POST['frame'];
$sname=$_POST['sname'];
$contact=$_POST['pnumber'];
$dob=$_POST['bday'];

echo "<br>";


echo $sql="SELECT*from student where NUMBER='$contact'";
$query=mysqli_query($connect,$sql);
if($query)
 {
   echo"hii";
   $row=mysqli_fetch_array($query);
if($row>0){
  echo"i am hridoy";
 }
 echo "<br>";
 echo "<table>";
 echo "<tr>";
 echo "<th>";
 echo "Name";
 echo "</th>";
 echo "<th>";
 echo "surName";
 echo "</th>";
 echo "<th>";
 echo "number";
 echo "</th>";
 echo "<th>";
 echo "dob";
 echo "</th>";
 echo "</tr>";
 echo "<tr>";
 echo "<td>";
 echo $row['name'];
 echo "</td>";
 

}
?>