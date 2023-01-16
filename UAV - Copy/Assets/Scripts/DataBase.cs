using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using MongoDB.Bson;
using MongoDB.Driver;
using System.Threading.Tasks;

public class DataBase : MonoBehaviour
{
    MongoClient client = new MongoClient("mongodb+srv://deniz:727302dk@cluster0.zuwnt7e.mongodb.net/?retryWrites=true&w=majority");
    IMongoDatabase database;
    IMongoCollection<BsonDocument> collection, collectionIkas;

    Sensor sensor;
    SensorIka sensorIka;
    MoveUAV moveUAV;
    MoveTank moveTank;
    ControlPanel controlPanel;

    string[] İHA = new string[] {"İHA1","İHA2","İHA3","İHA4","İHA5","İHA6","İHA7","İHA8","İHA9","İHA10","İHA11","İHA12","İHA13","İHA14","İHA15","İHA16"};
    string[] İKA = new string[] {"İKA1","İKA2","İKA3","İKA4","İKA5","İKA6","İKA7","İKA8","İKA9","İKA10","İKA11","İKA12","İKA13","İKA14","İKA15","İKA16"};


    void Start()
    {
        database = client.GetDatabase("test");
        collection = database.GetCollection<BsonDocument>("ihas");
        collectionIkas = database.GetCollection<BsonDocument>("ikas");
        controlPanel = GameObject.Find("ControlPanel").GetComponent<ControlPanel>();

/*
        new MongoClient("mongodb+srv://deniz:727302dk@cluster0.zuwnt7e.mongodb.net/?retryWrites=true&w=majority").GetDatabase("test").GetCollection<BsonDocument>("ihas").InsertOne(new BsonDocument{
            {"name", "iha1"},
            {"e-x", 50},
            {"e-nx", 200},
            {"e-y", 200},
            {"e-ny", 200},
            {"e-z", 200},
            {"e-nz", 200},
            {"status", 1}
        });
        new MongoClient("mongodb+srv://deniz:727302dk@cluster0.zuwnt7e.mongodb.net/?retryWrites=true&w=majority").GetDatabase("test").GetCollection<BsonDocument>("ihas").InsertOne(new BsonDocument{
            {"name", "iha2"},
            {"e-x", 50},
            {"e-nx", 200},
            {"e-y", 200},
            {"e-ny", 200},
            {"e-z", 200},
            {"e-nz", 200},
            {"status", 1}
        });
*/
/*
        //filtrelenen dokumanı değşitirir
        var filter1 = Builders<BsonDocument>.Filter.Eq("name", "İHA1");
        var update1 = Builders<BsonDocument>.Update.Set("e_x", 11111);

        collection.UpdateOne(filter1, update1);

        var filter2 = Builders<BsonDocument>.Filter.Eq("name", "İHA2");
        var update2 = Builders<BsonDocument>.Update.Set("e_x", 222222);

        collection.UpdateOne(filter2, update2);


        //filtrelenen dokümanı getirir
        
        var ihaDocument1 = collection.Find(filter1).FirstOrDefault();
        var ihaDocument2 = collection.Find(filter2).FirstOrDefault();
*/
        


        
/*
        //tüm dökümanları götürür
        var documents = collection.Find(new BsonDocument()).ToList();
         foreach(BsonDocument doc in documents)
        {
            Debug.Log(doc);
        }       
*/

    }
/*
    public class VerilerZ
    {
        public string name { get; set; }
        public int e_x { get; set; }
        public int e_nx { get; set; }
        public int e_y { get; set; }
        public int e_ny { get; set; }
        public int e_z { get; set; }
        public int e_nz { get; set; }
        public int status { get; set; }
    
        Debug.Log(;
    }
*/

    public void veriAlButton()
    {
        /*
        var filter1 = Builders<BsonDocument>.Filter.Eq("name", "İHA1");
        var ihaDocument1 = collection.Find(filter1).FirstOrDefault();

        moveUAV = GameObject.Find("UAV0").GetComponent<MoveUAV>();

        moveUAV.s_x = ihaDocument1["s_x"].ToInt32();
        moveUAV.s_y = ihaDocument1["s_y"].ToInt32();
        moveUAV.s_z = ihaDocument1["s_z"].ToInt32();
        moveUAV.target = new Vector3(moveUAV.s_x, moveUAV.s_y, moveUAV.s_z);
//---------------
        var filter2 = Builders<BsonDocument>.Filter.Eq("name", "İHA2");
        var ihaDocument2 = collection.Find(filter2).FirstOrDefault();

        moveUAV = GameObject.Find("UAV1").GetComponent<MoveUAV>();

        moveUAV.s_x = ihaDocument2["s_x"].ToInt32();
        moveUAV.s_y = ihaDocument2["s_y"].ToInt32();
        moveUAV.s_z = ihaDocument2["s_z"].ToInt32();
        moveUAV.target = new Vector3(moveUAV.s_x, moveUAV.s_y, moveUAV.s_z);
        */


        //StartCoroutine(CoroutineTest());
    }

    private void FixedUpdate()
    {
        /*
                //En yakın araç mesafe GONDER
                if(UAVsensor[i].enKucukYon == "Sag")
                {
                    collection.UpdateOne(IHAfilter[i], Builders<BsonDocument>.Update.Set("a_z", Mathf.CeilToInt(UAVsensor[i].enKucuk)));
                }
                else if(UAVsensor[i].enKucukYon == "Sol")
                {
                    collection.UpdateOne(IHAfilter[i], Builders<BsonDocument>.Update.Set("a_nz", Mathf.CeilToInt(UAVsensor[i].enKucuk)));
                }
                else if(UAVsensor[i].enKucukYon == "On")
                {
                    collection.UpdateOne(IHAfilter[i], Builders<BsonDocument>.Update.Set("a_x", Mathf.CeilToInt(UAVsensor[i].enKucuk)));
                }
                else if(UAVsensor[i].enKucukYon == "Arka")
                {
                    collection.UpdateOne(IHAfilter[i], Builders<BsonDocument>.Update.Set("a_nx", Mathf.CeilToInt(UAVsensor[i].enKucuk)));
                }
                else if(UAVsensor[i].enKucukYon == "Ust")
                {
                    collection.UpdateOne(IHAfilter[i], Builders<BsonDocument>.Update.Set("a_y", Mathf.CeilToInt(UAVsensor[i].enKucuk)));
                }
                else if(UAVsensor[i].enKucukYon == "Alt")
                {
                    collection.UpdateOne(IHAfilter[i], Builders<BsonDocument>.Update.Set("a_ny", Mathf.CeilToInt(UAVsensor[i].enKucuk)));
                }



                //En yakın araç engel GONDER
                if(UAVsensor[i].enKucukEngelYon == "Sag")
                {                  
                    collection.UpdateOne(IHAfilter[i], Builders<BsonDocument>.Update.Set("e_z", Mathf.CeilToInt(UAVsensor[i].enKucukEngel)));
                }
                else if(UAVsensor[i].enKucukEngelYon == "Sol")
                {                   
                    collection.UpdateOne(IHAfilter[i], Builders<BsonDocument>.Update.Set("e_nz", Mathf.CeilToInt(UAVsensor[i].enKucukEngel)));
                }
                else if(UAVsensor[i].enKucukEngelYon == "On")
                {                   
                    collection.UpdateOne(IHAfilter[i], Builders<BsonDocument>.Update.Set("e_x", Mathf.CeilToInt(UAVsensor[i].enKucukEngel)));
                }
                else if(UAVsensor[i].enKucukEngelYon == "Arka")
                {              
                    collection.UpdateOne(IHAfilter[i], Builders<BsonDocument>.Update.Set("e_nx", Mathf.CeilToInt(UAVsensor[i].enKucukEngel)));
                }
                else if(UAVsensor[i].enKucukEngelYon == "Ust")
                {           
                    collection.UpdateOne(IHAfilter[i], Builders<BsonDocument>.Update.Set("e_y", Mathf.CeilToInt(UAVsensor[i].enKucukEngel)));
                }
                else if(UAVsensor[i].enKucukEngelYon == "Alt")
                {
                    collection.UpdateOne(IHAfilter[i], Builders<BsonDocument>.Update.Set("e_ny", Mathf.CeilToInt(UAVsensor[i].enKucukEngel)));
                }
*/
/*
                collection.UpdateOne(IHAfilter[i], Builders<BsonDocument>.Update.Set("a_z", Mathf.CeilToInt(UAVsensor[i].a_z)));
                collection.UpdateOne(IHAfilter[i], Builders<BsonDocument>.Update.Set("a_nz", Mathf.CeilToInt(UAVsensor[i].a_nz)));
                collection.UpdateOne(IHAfilter[i], Builders<BsonDocument>.Update.Set("a_x", Mathf.CeilToInt(UAVsensor[i].a_x)));
                collection.UpdateOne(IHAfilter[i], Builders<BsonDocument>.Update.Set("a_nx", Mathf.CeilToInt(UAVsensor[i].a_nx)));
                collection.UpdateOne(IHAfilter[i], Builders<BsonDocument>.Update.Set("a_y", Mathf.CeilToInt(UAVsensor[i].a_y)));
                collection.UpdateOne(IHAfilter[i], Builders<BsonDocument>.Update.Set("a_ny", Mathf.CeilToInt(UAVsensor[i].a_ny)));

                collection.UpdateOne(IHAfilter[i], Builders<BsonDocument>.Update.Set("e_z", Mathf.CeilToInt(UAVsensor[i].e_z)));
                collection.UpdateOne(IHAfilter[i], Builders<BsonDocument>.Update.Set("e_nz", Mathf.CeilToInt(UAVsensor[i].e_nz)));
                collection.UpdateOne(IHAfilter[i], Builders<BsonDocument>.Update.Set("e_x", Mathf.CeilToInt(UAVsensor[i].e_x)));
                collection.UpdateOne(IHAfilter[i], Builders<BsonDocument>.Update.Set("e_nx", Mathf.CeilToInt(UAVsensor[i].e_nx)));
                collection.UpdateOne(IHAfilter[i], Builders<BsonDocument>.Update.Set("e_y", Mathf.CeilToInt(UAVsensor[i].e_y)));
                collection.UpdateOne(IHAfilter[i], Builders<BsonDocument>.Update.Set("e_ny", Mathf.CeilToInt(UAVsensor[i].e_ny)));
            */
                      
               /* //aracın gidecek konumlarını AL
                UAVmove[i].s_x = collection.Find(IHAfilter[i]).FirstOrDefault()["s_x"].ToInt32();
                UAVmove[i].s_y = collection.Find(IHAfilter[i]).FirstOrDefault()["s_y"].ToInt32();
                UAVmove[i].s_z = collection.Find(IHAfilter[i]).FirstOrDefault()["s_z"].ToInt32();*/

        //İhlar 5 saniyede bir hedefleri güncellenir.
        for (int i = 0; i < controlPanel.uavS; i++)
        {
            var filter = Builders<BsonDocument>.Filter.Eq("name", İHA[i]);
            var ihaDocument = collection.Find(filter).FirstOrDefault();
    
            moveUAV = GameObject.Find(İHA[i]).GetComponent<MoveUAV>();
            sensor = GameObject.Find(İHA[i]).GetComponentInChildren<Sensor>();
    /*
            //aracın gidecek konumlarını AL
            moveUAV.s_x = ihaDocument["s_x"].ToInt32();
            moveUAV.s_y = ihaDocument["s_y"].ToInt32();
            moveUAV.s_z = ihaDocument["s_z"].ToInt32();
            moveUAV.target = new Vector3(moveUAV.s_x, moveUAV.s_y, moveUAV.s_z);
    */
    
    
            //En yakın araç mesafe GONDER
            if(sensor.enKucukYon == "Sag")
            {
                var update = Builders<BsonDocument>.Update.Set("a_z", Mathf.CeilToInt(sensor.enKucuk));
                collection.UpdateOne(filter, update);
            }
            else if(sensor.enKucukYon == "Sol")
            {
                var update = Builders<BsonDocument>.Update.Set("a_nz", Mathf.CeilToInt(sensor.enKucuk));
                collection.UpdateOne(filter, update);
            }
            else if(sensor.enKucukYon == "On")
            {
                var update = Builders<BsonDocument>.Update.Set("a_x", Mathf.CeilToInt(sensor.enKucuk));
                collection.UpdateOne(filter, update);
            }
            else if(sensor.enKucukYon == "Arka")
            {
                var update = Builders<BsonDocument>.Update.Set("a_nx", Mathf.CeilToInt(sensor.enKucuk));
                collection.UpdateOne(filter, update);
            }
            else if(sensor.enKucukYon == "Ust")
            {
                var update = Builders<BsonDocument>.Update.Set("a_y", Mathf.CeilToInt(sensor.enKucuk));
                collection.UpdateOne(filter, update);
            }
            else if(sensor.enKucukYon == "Alt")
            {
                var update = Builders<BsonDocument>.Update.Set("a_ny", Mathf.CeilToInt(sensor.enKucuk));
                collection.UpdateOne(filter, update);
            }
    
            //En yakın araç engel GONDER
            if(sensor.enKucukEngelYon == "Sag")
            {
                var update = Builders<BsonDocument>.Update.Set("e_z", Mathf.CeilToInt(sensor.enKucuk));
                collection.UpdateOne(filter, update);
            }
            else if(sensor.enKucukEngelYon == "Sol")
            {
                var update = Builders<BsonDocument>.Update.Set("e_nz", Mathf.CeilToInt(sensor.enKucuk));
                collection.UpdateOne(filter, update);
            }
            else if(sensor.enKucukEngelYon == "On")
            {
                var update = Builders<BsonDocument>.Update.Set("e_x", Mathf.CeilToInt(sensor.enKucuk));
                collection.UpdateOne(filter, update);
            }
            else if(sensor.enKucukEngelYon == "Arka")
            {
                var update = Builders<BsonDocument>.Update.Set("e_nx", Mathf.CeilToInt(sensor.enKucuk));
                collection.UpdateOne(filter, update);
            }
            else if(sensor.enKucukEngelYon == "Ust")
            {
                var update = Builders<BsonDocument>.Update.Set("e_y", Mathf.CeilToInt(sensor.enKucuk));
                collection.UpdateOne(filter, update);
            }
            else if(sensor.enKucukEngelYon == "Alt")
            {
                var update = Builders<BsonDocument>.Update.Set("e_ny", Mathf.CeilToInt(sensor.enKucuk));
                collection.UpdateOne(filter, update);
            }
    
    
    
    
    
            
    
    
        }
        for (int i = 0; i < controlPanel.tankS; i++)
        {
            var filter = Builders<BsonDocument>.Filter.Eq("name", İKA[i]);
            var ikaDocument = collectionIkas.Find(filter).FirstOrDefault();
    
            moveTank = GameObject.Find(İKA[i]).GetComponent<MoveTank>();
            sensorIka = GameObject.Find(İKA[i]).GetComponentInChildren<SensorIka>();
    /*
            moveTank.s_x = ikaDocument["s_x"].ToInt32();
            moveTank.s_y = ikaDocument["s_y"].ToInt32();
            moveTank.s_z = ikaDocument["s_z"].ToInt32();
            moveTank.target = new Vector3(moveTank.s_x, moveTank.s_y, moveTank.s_z);
    */
    
            //En yakın araç mesafe GONDER
            if(sensorIka.enKucukYon == "Sag")
            {
                var update = Builders<BsonDocument>.Update.Set("a_z", Mathf.CeilToInt(sensorIka.enKucuk));
                collectionIkas.UpdateOne(filter, update);
            }
            else if(sensorIka.enKucukYon == "Sol")
            {
                var update = Builders<BsonDocument>.Update.Set("a_nz", Mathf.CeilToInt(sensorIka.enKucuk));
                collectionIkas.UpdateOne(filter, update);
            }
            else if(sensorIka.enKucukYon == "On")
            {
                var update = Builders<BsonDocument>.Update.Set("a_x", Mathf.CeilToInt(sensorIka.enKucuk));
                collectionIkas.UpdateOne(filter, update);
            }
            else if(sensorIka.enKucukYon == "Arka")
            {
                var update = Builders<BsonDocument>.Update.Set("a_nx", Mathf.CeilToInt(sensorIka.enKucuk));
                collectionIkas.UpdateOne(filter, update);
            }
    
            //En yakın araç engel GONDER
            if(sensorIka.enKucukEngelYon == "Sag")
            {
                var update = Builders<BsonDocument>.Update.Set("e_z", Mathf.CeilToInt(sensorIka.enKucuk));
                collectionIkas.UpdateOne(filter, update);
            }
            else if(sensorIka.enKucukEngelYon == "Sol")
            {
                var update = Builders<BsonDocument>.Update.Set("e_nz", Mathf.CeilToInt(sensorIka.enKucuk));
                collectionIkas.UpdateOne(filter, update);
            }
            else if(sensorIka.enKucukEngelYon == "On")
            {
                var update = Builders<BsonDocument>.Update.Set("e_x", Mathf.CeilToInt(sensorIka.enKucuk));
                collectionIkas.UpdateOne(filter, update);
            }
            else if(sensorIka.enKucukEngelYon == "Arka")
            {
                var update = Builders<BsonDocument>.Update.Set("e_nx", Mathf.CeilToInt(sensorIka.enKucuk));
                collectionIkas.UpdateOne(filter, update);
            }
    
        }
    
        //yield return new WaitForSeconds( 3f ); // 1 saniye bekle 0.1 saniye
        //StartCoroutine(CoroutineTest());
    
    }
   

    

}
