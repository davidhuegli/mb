<?php
include 'conf.php';

//echo $mysql_host;

if ($_SERVER["REQUEST_METHOD"] == "POST") {//Check it is comming from a form

	
	$u_name = filter_var($_POST["user_name"], FILTER_SANITIZE_STRING); //set PHP variables like this so we can use them anywhere in code below
	$u_password = filter_var($_POST["user_password"], FILTER_SANITIZE_STRING);
	
	$hash = hash(sha256, $u_password);
	//echo " <br> $hash";	

// Create connection
$conn = new mysqli($mysql_host, $mysql_username, $mysql_password, $mysql_database);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT pwhash FROM users WHERE username='$u_name'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
	//echo "<br>PW HASH from DB: " . $row["pwhash"]. "<br>";
	if ($hash == $row["pwhash"]) {
		echo "Login erfolgreich, Weiterleitung erfolgt!";
		session_start();   
		$sessionid = session_id();
		echo " <br> SessionID: " . $sessionid;
		$sql = "UPDATE 'users' SET 'sessionid' = $sessionid WHERE 'users'.'username' = $u_name";

		if ($conn->query($sql) === TRUE) {
 		 echo "New record created successfully";
		} else {
		  echo "Error: " . $sql . "<br>" . $conn->error;
		}
		//$sql = "INSERT INTO users (session_id) VALUES ('session_id()') WHERE username='$u_name'";
		header( "refresh:5;url=quiz.php" );
		
	}else{
		echo "Passwort und/oder Nutzername nicht korrekt!       Weiterleitung erfolgt!";
		header( "refresh:5;url=index.html" );
	}

  }
} else {
  echo "<br> User nicht vorhanden oder Passwort falsch ;-)";
}
$conn->close();


}
?>