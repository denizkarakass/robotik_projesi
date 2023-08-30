import './App.css';
import { useState } from 'react';
import {useNavigate} from 'react-router-dom'; 

function İniş() {

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
      İniş  Kordinaatları Giriş Formu   
        <div className="form-group">
          <label htmlFor="yangınx" className="form-label">X</label>
          <input className="form-control" name="yangınx" onChange={onChangeHandler} value={formData.inişx} />
        </div>
        <div className="form-group">
          <label htmlFor="yangıny" className="form-label">Y</label>
          <input className="form-control" name="yangıny" onChange={onChangeHandler} value={formData.inişy} />
        </div>
        <div className="form-group">
          <label htmlFor="yangınz" className="form-label">Z</label>
          <input className="form-control" name="yangınz" onChange={onChangeHandler} value={formData.inişz} />
        </div>
      
        
        
        <div className="form-group">
          <button className="btn "onClick={() => navigate("/")} type="submit" >Veriyi Gönder</button>
        </div>
      </form>
    </div>
  );
}

export default İniş;
