# SETUP Token API
#### 1. Tambahkan Fungsi pada file database.php
```
public function token()
{
    date_default_timezone_set('Asia/Jakarta');
    $kode = "secret_kode";    
    $today = date("Y-m-d");
    $val = MD5($kode . $today);
    return $val;
}
```
#### 2. Tambahkan variabel untuk menampung token yang valid pada file mahasiswa_api.php
```
$method = $_SERVER['REQUEST_METHOD'];
$valid_token = $db->token();
```
