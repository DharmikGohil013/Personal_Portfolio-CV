<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST, GET, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type, Authorization");


$to = 'dharmikgohil395003@example.com';
$subject = $_POST['subject'];
$message = $_POST['message'];
$headers = "From: " . $_POST['email'];

if(mail($to, $subject, $message, $headers)) {
    echo 'Message sent successfully!';
} else {
    echo 'Failed to send message.';
}
?>
