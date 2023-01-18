import './App.css';
import { useState } from 'react';

function İniş() {

  const [formData, setFormData] = useState({
    inişx: 'X değerini giriniz',
    inişy: 'Y değerini giriniz',
    inişz: 'Z değerini giriniz'
    
  })

  const onChangeHandler = (event) => {

    console.log(event)
    if (event.target.name === 'languages') {

      let copy = { ...formData }

      if (event.target.checked) {
        copy.languages.push(event.target.value)
      } else {
        copy.languages = copy.languages.filter(el => el !== event.target.value)
      }

      setFormData(copy)

    } else {
      setFormData(() => ({
        ...formData,
        [event.target.name]: event.target.value
      }))
    }
  }

  const onSubmitHandler = (event) => {
    event.preventDefault()
    console.log(formData)
  }
  return (
    <div className="App">
      <form onSubmit={onSubmitHandler}>
      İniş koordinatları Giriş Formu 
        <div className="form-group">
        
          <label htmlFor="inişx" className="form-label">X</label>
          <input className="form-control" name="inişx" onChange={onChangeHandler} value={formData.inişx} />
        </div>
        <div className="form-group">
          <label htmlFor="inişy" className="form-label">Y</label>
          <input className="form-control" name="inişx" onChange={onChangeHandler} value={formData.inişy} />
        </div>
        <div className="form-group">
          <label htmlFor="inişz" className="form-label">Z</label>
          <input className="form-control" name="inişx" onChange={onChangeHandler} value={formData.inişz} />
        </div>
        <input type={'hidden'} className="form-control" name="inişx" onChange={onChangeHandler}  />
        
        <div className="form-group">
          <button className="btn" type="submit"  >Veriyi Gönder</button>
        </div>
      </form>
    </div>
  );
}

export default İniş;
