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
