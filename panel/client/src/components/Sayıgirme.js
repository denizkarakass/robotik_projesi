import './App.css';
import { useState } from 'react';

function Sayıgirme() {

  const [formData, setFormData] = useState({
    IHASAYISI: 'IHA Sayısı Giriniz',
    IKASAYISI: 'IKA Sayısı Giriniz',
    
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
          <button className="btn" type="submit" class="btn " >Veriyi Gönder</button>
        </div>
      </form>
    </div>
  );
}

export default Sayıgirme;
