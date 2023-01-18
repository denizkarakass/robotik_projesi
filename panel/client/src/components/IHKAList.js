import React from 'react';
const IHKAList = (props) => {
           return (
            <div className="row">
                {props.IHKAs.map((IHKA) => (
                    <div className="col-lg-4" key={IHKA.id}>
                        <div className="card mb-4 shadow-sm">
                                 <div className="card-body">
                                 <h5 className="card-title">{IHKA.name}</h5>
                                 <p className="card-text">{IHKA.konumx}</p>
                                 <p className="card-text">{IHKA.konumy}</p>
                                 <p className="card-text">{IHKA.konumz}</p>
                                 <div className="d-flex justify-content-between align-items-center">
                                    <button type="button" onClick={(event) => props.deleteIHKAProp(IHKA)} className="btn btn-md btn-outline-danger">Delete</button>
                                </div>
                            </div>
                        </div>
                    </div>

                ))}

            </div>
        )
}

export default IHKAList;