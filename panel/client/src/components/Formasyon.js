import './App.css';
import { useState } from 'react';


function App() {

  const [formData, setFormData] = useState({
   Formasyon: ['Seçiniz'],
  })

  const onChangeHandler = (event) => {

    console.log(event)
    if (event.target.name === 'Formasyon') {

      let copy = { ...formData }

      if (event.target.checked) {
        copy.Formasyon.push(event.target.value)
      } else {
        copy.Formasyon = copy.Formasyon.filter(el => el !== event.target.value)
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
          <label htmlFor="Formasyon" className="form-label">Formasyon Seçiniz</label>
          <div>
            <div>
              <input type="checkbox" name="Formasyon" value="Meşale" onChange={onChangeHandler} checked={formData.Formasyon.indexOf('Meşale') !== -1} />
              <label htmlFor="Meşale">Meşale</label>
            </div>
            <div>
              <input type="checkbox" name="Formasyon" value="Okçunun Oku" onChange={onChangeHandler} checked={formData.Formasyon.indexOf('Okçunun Oku') !== -1} />
              <label htmlFor="Okçunun Oku">Okçunun Oku</label>
            </div>
            
          </div>
        </div>
        
        <div className="form-group">
          <button className="btn " type="submit" >Veriyi Gönder</button>
        </div>
      </form>
    </div>
  );
}

export default App;