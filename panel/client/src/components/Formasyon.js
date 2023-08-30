import './App.css';
import { useState } from 'react';
import {useNavigate} from 'react-router-dom'; 

function Formasyon() {

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
      Formasyon seçme formu   
      <div className="form-group">
          <label htmlFor="occupation" className="form-label">Formasyon Seçiniz</label>
          <select className="form-select" name="occupation" onChange={onChangeHandler} value={formData.occupation}>
            <option value="student">Meşale</option>
            <option value="employee">Okçunun Oku</option>
                      </select>
        </div>
         
        <div className="form-group">
          <button className="btn "onClick={() => navigate("/")} type="submit" >Veriyi Gönder</button>
        </div>
      </form>
    </div>
  );
}

export default Formasyon;
