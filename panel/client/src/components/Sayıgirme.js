import './App.css';
import { useState } from 'react';
import {useNavigate} from 'react-router-dom'; 
function Sayıgirme() {

  const [formData, setFormData] = useState({
    
    
  })
const onChangeHandler = (event) => {
       setFormData(() => ({
     ...formData,
     [event.target.name]: event.target.value
   }))
 }
 const onSubmitHandler = (event) => {
 event.preventDefault()
 console.log(formData)
}
const navigate = useNavigate();
  return (
    <div className="App">
      <form onSubmit={onSubmitHandler}>
        <div className="form-group">
          <div> Aktif İHA İKA Giriş Formu </div>
          <label htmlFor="IHASAYISI" className="form-label">IHA sayısı</label>
          <input className="form-control" name="IHASAYISI" onChange={onChangeHandler} value={formData.IHASAYISI} />
        </div>
        <div className="form-group">
          <label htmlFor="IKASAYISI" className="form-label">IKA Sayısı</label>
          <input className="form-control" name="IKASAYISI" onChange={onChangeHandler} value={formData.IKASAYISI} />
        </div>
        
        
        <div className="form-group">
          <button className="btn "onClick={() => navigate("/")} type="submit" >Veriyi Gönder</button>
        </div>
      </form>
    </div>
  );
}

export default Sayıgirme;
