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
#### 2. Tambahkan variabel $valid_token untuk menampung token yang valid pada file mahasiswa_api.php
```
$method = $_SERVER['REQUEST_METHOD'];
$valid_token = $db->token();
```
#### 3. Revisi kode program untuk metode GET
```
case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nim'])){
            $nim = $_GET['nim'];
        }
        if(isset($_GET['token'])){
            $token = $_GET['token'];
        }
        if($token !== $valid_token){
            $val['status']='failed';
            $val['message']='Token not valid';
        }else{
            if($id>0){    
                $result = $mahasiswa->get_by_id($id);
            }elseif($nim>0){
                $result = $mahasiswa->get_by_nim($nim);
            } else {
                $result = $mahasiswa->get_all();
            }    
            $val = array();
            while ($row = $result->fetch_assoc()) {
                $val[] = $row;
            }
        }
              
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
```
#### 4. Revisi kode program untuk metode POST pada file mahasiswa_api.php
```
case 'POST':
        // Add a new mahasiswa
        $mahasiswa->nim = $_POST['nim'];
        $mahasiswa->nama = $_POST['nama'];
        $mahasiswa->jk = $_POST['jk'];
        $mahasiswa->prodi = $_POST['prodi'];
        $token = $_POST['token'];

        if($token !== $valid_token){
            $data['status']='failed';
            $data['message']='Token not valid';
        }else{
            $mahasiswa->insert();
            $a = $db->affected_rows();
            if($a>0){
                $data['status']='success';
                $data['message']='Data Mahasiswa created successfully.';
            } else {
                $data['status']='failed';
                $data['message']='Data Mahasiswa not created.';
            }
        }
        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
```
#### 5. Revisi Kode program untuk metode PUT pada file mahasiswa_api.php
```
case 'PUT':
        // Update an existing data
        $_PUT = [];
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nim'])){
            $nim = $_GET['nim'];
        }
    
        parse_str(file_get_contents("php://input"), $_PUT);
        $mahasiswa->nim = $_PUT['nim'];
        $mahasiswa->nama = $_PUT['nama'];
        $mahasiswa->jk = $_PUT['jk'];
        $mahasiswa->prodi = $_PUT['prodi'];
        $token = $_PUT['token'];
        if($token !== $valid_token){
            $data['status']='failed';
            $data['message']='Token not valid';
        }else{
            if($id>0){    
                $mahasiswa->update($id);
            }elseif($nim<>""){
                $mahasiswa->update_by_nim($nim);
            } else {
                
            } 
            $a = $db->affected_rows();
            if($a>0){
                $data['status']='success';
                $data['message']='Data Mahasiswa updated successfully.';
            } else {
                $data['status']='failed';
                $data['message']='Data Mahasiswa update failed.';
            } 
        }
               
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
```
#### 6. Revisi kode program untuk metode DELETE pada file mahasiswa_api.php
```
case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nim'])){
            $nim = $_GET['nim'];
        }
        if(isset($_GET['token'])){
            $token = $_GET['token'];
        }
        if($token !== $valid_token){
            $data['status']='failed';
            $data['message']='Token not valid';
        }else{

            if($id>0){    
                $mahasiswa->delete($id);
            }elseif($nim>0){
                $mahasiswa->delete_by_nim($nim);
            } else {
                
            }             
            $a = $db->affected_rows();
            if($a>0){
                $data['status']='success';
                $data['message']='Data Mahasiswa deleted successfully.';
            } else {
                $data['status']='failed';
                $data['message']='Data Mahasiswa delete failed.';
            }
        }
                
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
```
