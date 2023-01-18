import React from 'react';
import IHKAList from './IHKAList';
import SearchBar from './SearchBar';
import Yangın from './Yangın';
import İniş from './İniş';
import Sayıgirme from './Sayıgirme';
import Formasyon from './Formasyon';
import axios from 'axios';
import './App.css';
import { BrowserRouter as Router, Routes, Route,} from "react-router-dom";

class App extends React.Component {
    state = {
        IHKAs: [],
        searchQuery: ""
    }
    async componentDidMount() {
        const response = await axios.get("http://localhost:3002/IHKAs");
        this.setState({IHKAs: response.data})
    }
    //Delete IHKA
    deleteIHKA =  async (IHKA) => {
        axios.delete(`http://localhost:3002/IHKAs/${IHKA.id}`)
        const newIHKAList = this.state.IHKAs.filter(
            m => m.id !== IHKA.id
        );
        this.setState(state => ({
            IHKAs: newIHKAList
        }))
    } 
    //SEARCH IHKA
    searchIHKA = (event) => {
        this.setState({searchQuery: event.target.value })
    }
    //ADD IHKA
    addIHKA = async (IHKA) => {
        await axios.post(`http://localhost:3002/IHKAs`, IHKA)
        console.log(IHKA)
        this.setState(state => ({
            IHKAs:state.IHKAs.concat([IHKA])
        }))
    }
    render() {
        console.log(this.state.IHKAs)
        let filteredIHKAs = this.state.IHKAs.filter(
            (IHKA) => {
                return IHKA.name.toLowerCase().indexOf(this.state.searchQuery.toLowerCase()) !== -1
            }
        )

        return (
            <Router>
                
                <Routes>
                <Route path="/" element={
                  <React.Fragment>
                  <div className="container">
                    <div className="row">
                      <div className="col-lg-12">
                        <SearchBar searchIHKAProp={this.searchIHKA} />
                      </div>
                    </div>
                    <IHKAList
                      IHKAs={filteredIHKAs}
                      deleteIHKAProp={this.deleteIHKA}
                    />
                    </div>
                    </React.Fragment>
                }> 
                
                </Route>
                <React.Fragment>
                <Route path="yangın" element={
                        <Yangın 
                            onYangın = {(IHKA) => {this.Yangın(IHKA)}}
                        />
                    } />
                    </React.Fragment>

                    <React.Fragment>
                <Route path="iniş" element={
                        <İniş 
                            onİniş = {(IHKA) => {this.İniş(IHKA)}}
                        />
                    } />
                    </React.Fragment>
                    <React.Fragment>
                <Route path="sayıgirme" element={
                        <Sayıgirme
                            onSayıgirme = {(IHKA) => {this.Sayıgirme(IHKA)}}
                        />
                    } />
                    </React.Fragment>
                    <React.Fragment>
                <Route path="formasyon" element={
                        <Formasyon
                            onFormasyon = {(IHKA) => {this.Formasyon(IHKA)}}
                        />
                    } />
                    </React.Fragment>
                    
                </Routes>
            </Router>
          );
    }
}
export default App;