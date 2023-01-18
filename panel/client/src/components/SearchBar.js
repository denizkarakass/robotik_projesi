import React from 'react';
import { Link } from 'react-router-dom';
class SearchBar extends React.Component {
    handleFormSubmit = (event) => {
        event.preventDefault();
    }

    render() {

        return  (
          <form onSubmit={(event) => event.preventDefault()}>
        <div className="form-row mb-5">
          <div className="container">
            <div className="row">
              <div className="col-10">
                <input
                  onChange={this.props.searchIKHAProp}
                  type="text"
                  className="form-control"
                  placeholder="Search a IKHA"
                />
              </div>
              <div className="col-2">
              
              <Link to="/yangın" className="link-btn btn btn-md btn-danger" style={{float:'right'}}>Yangın Koordinatlarını giriş</Link>
              <Link to="/iniş" className="link-btn btn btn-md btn-danger" style={{float:'right'}}>İniş Koordinatlarını giriş</Link>
              <Link to="/sayıgirme" className="link-btn btn btn-md btn-danger" style={{float:'right'}}>Aktif IHKA sayısı giriş</Link>
              <Link to="/formasyon" className="link-btn btn btn-md btn-danger"  style={{float:'right'}}>Formasyon giriş</Link>

                  
                  
              </div>
            </div>
          </div>
        </div>
      </form>
  
        )

    }
}


export default SearchBar;