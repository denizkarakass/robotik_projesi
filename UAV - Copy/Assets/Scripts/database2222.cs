using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using MongoDB.Bson;
using MongoDB.Driver;
using System.Threading.Tasks;

public class database2222 : MonoBehaviour
{
    MongoClient client = new MongoClient("mongodb+srv://deniz:727302dk@cluster0.zuwnt7e.mongodb.net/?retryWrites=true&w=majority");
    IMongoDatabase database;
    IMongoCollection<BsonDocument> collection, collectionIkas;
    MongoDB.Driver.FilterDefinition<MongoDB.Bson.BsonDocument>[] IHAfilter = new MongoDB.Driver.FilterDefinition<MongoDB.Bson.BsonDocument>[16];
    MongoDB.Driver.FilterDefinition<MongoDB.Bson.BsonDocument>[] İKAfilter = new MongoDB.Driver.FilterDefinition<MongoDB.Bson.BsonDocument>[16];
    MongoDB.Driver.FilterDefinition<MongoDB.Bson.BsonDocument>[] IHAdocument = new MongoDB.Driver.FilterDefinition<MongoDB.Bson.BsonDocument>[16];
    MongoDB.Driver.FilterDefinition<MongoDB.Bson.BsonDocument>[] İKAdocument = new MongoDB.Driver.FilterDefinition<MongoDB.Bson.BsonDocument>[16];

    MoveUAV[] UAVmove = new MoveUAV[16];
    MoveTank[] IKAmove = new MoveTank[16];
    Sensor[]  UAVsensor = new Sensor[16];
    SensorIka[] IKAsensor = new SensorIka[16];


    //Sensor sensor;
    //SensorIka sensorIka;
    //MoveUAV moveUAV;
    //MoveTank moveTank;
    ControlPanel controlPanel;

    string[] İHA = new string[] {"İHA1","İHA2","İHA3","İHA4","İHA5","İHA6","İHA7","İHA8","İHA9","İHA10","İHA11","İHA12","İHA13","İHA14","İHA15","İHA16"};
    string[] İKA = new string[] {"İKA1","İKA2","İKA3","İKA4","İKA5","İKA6","İKA7","İKA8","İKA9","İKA10","İKA11","İKA12","İKA13","İKA14","İKA15","İKA16"};

    //object[] IHAfilter = new object[16];
    //object[] İKAfilter = new object[16];
    //object[] IHAdocument = new object[16];
    //object[] İKAdocument = new object[16];

    bool veriAl = false;

    private void Start() {
    }




    private void veriAlButton()
    {
        database = client.GetDatabase("test");
        collection = database.GetCollection<BsonDocument>("ihas");
        collectionIkas = database.GetCollection<BsonDocument>("ikas");
        controlPanel = GameObject.Find("ControlPanel").GetComponent<ControlPanel>();

        for (int i = 0; i < controlPanel.uavS; i++)
        {
            IHAfilter[i] = Builders<BsonDocument>.Filter.Eq("name", İHA[i]);
            //IHAdocument[i] = collection.Find(IHAfilter[i]).FirstOrDefault();
            UAVmove[i] = GameObject.Find(İHA[i]).GetComponent<MoveUAV>();
            UAVsensor[i] = GameObject.Find(İHA[i]).GetComponentInChildren<Sensor>();
        }
        
        for (int i = 0; i < controlPanel.tankS; i++)
        {
            İKAfilter[i] = Builders<BsonDocument>.Filter.Eq("name", İKA[i]);
            //İKAdocument[i] = collectionIkas.Find(İKAfilter[i]).FirstOrDefault();
            IKAmove[i] = GameObject.Find(İKA[i]).GetComponent<MoveTank>();
            IKAsensor[i] = GameObject.Find(İKA[i]).GetComponentInChildren<SensorIka>();
        }

        veriAl = true;
        StartCoroutine(DataBekle());
    }
    IEnumerator DataBekle()
    {
        yield return new WaitForSeconds(1f);
        DataAl();
        Debug.Log("Veri Alındı");
    }
    async void DataAl()
    {
            //İhlar 5 saniyede bir hedefleri güncellenir.
            for (int i = 0; i < controlPanel.uavS; i++)
            {
                //aracın gidecek konumlarını AL
                var result = await collection.Find(IHAfilter[i]).FirstOrDefaultAsync();
                UAVmove[i].s_x = ((int)result["s_x"]);
                UAVmove[i].s_y = ((int)result["s_y"]);
                UAVmove[i].s_z = ((int)result["s_z"]);
                UAVmove[i].target = new Vector3(UAVmove[i].s_x, UAVmove[i].s_y, UAVmove[i].s_z);

                await collection.UpdateManyAsync
                (
                    IHAfilter[i],
                    new BsonDocument
                    {
                        { "$set", new BsonDocument
                            {
                                { "a_z", Mathf.CeilToInt(UAVsensor[i].a_z) },
                                { "a_nz", Mathf.CeilToInt(UAVsensor[i].a_nz) },
                                { "a_x", Mathf.CeilToInt(UAVsensor[i].a_x) },
                                { "a_nx", Mathf.CeilToInt(UAVsensor[i].a_nx) },
                                { "a_y", Mathf.CeilToInt(UAVsensor[i].a_y) },
                                { "a_ny", Mathf.CeilToInt(UAVsensor[i].a_ny) },

                                { "e_z", Mathf.CeilToInt(UAVsensor[i].e_z) },
                                { "e_nz", Mathf.CeilToInt(UAVsensor[i].e_nz) },
                                { "e_x", Mathf.CeilToInt(UAVsensor[i].e_x) },
                                { "e_nx", Mathf.CeilToInt(UAVsensor[i].e_nx) },
                                { "e_y", Mathf.CeilToInt(UAVsensor[i].e_y) },
                                { "e_ny", Mathf.CeilToInt(UAVsensor[i].e_ny) }
                            }
                        }
                    }
                );
                Debug.Log("İHA verileri güncellendi");

            
            
            }
            for (int i = 0; i < controlPanel.tankS; i++)
            {    
         
                //aracın gidecek konumlarını AL
                var result = await collectionIkas.Find(İKAfilter[i]).FirstOrDefaultAsync();
                IKAmove[i].s_x = ((int)result["s_x"]);
                IKAmove[i].s_y = ((int)result["s_y"]);
                IKAmove[i].s_z = ((int)result["s_z"]);
                IKAmove[i].target = new Vector3(IKAmove[i].s_x, IKAmove[i].s_y, IKAmove[i].s_z);
          
                 await collectionIkas.UpdateManyAsync
                (
                    İKAfilter[i],
                    new BsonDocument
                    {
                        { "$set", new BsonDocument
                            {
                                { "a_z", Mathf.CeilToInt(IKAsensor[i].a_z) },
                                { "a_nz", Mathf.CeilToInt(IKAsensor[i].a_nz) },
                                { "a_x", Mathf.CeilToInt(IKAsensor[i].a_x) },
                                { "a_nx", Mathf.CeilToInt(IKAsensor[i].a_nx) },

                                { "e_z", Mathf.CeilToInt(IKAsensor[i].e_z) },
                                { "e_nz", Mathf.CeilToInt(IKAsensor[i].e_nz) },
                                { "e_x", Mathf.CeilToInt(IKAsensor[i].e_x) },
                                { "e_nx", Mathf.CeilToInt(IKAsensor[i].e_nx) },
                            }
                        }
                    }
                );
                Debug.Log("İKA verileri güncellendi");
            }

        StartCoroutine(DataBekle());
    }

    

   /* async void FixedUpdate()
    {
        if (veriAl == true)
        {
            //İhlar 5 saniyede bir hedefleri güncellenir.
            for (int i = 0; i < controlPanel.uavS; i++)
            {
                //aracın gidecek konumlarını AL
                var result = await collection.Find(IHAfilter[i]).FirstOrDefaultAsync();
                UAVmove[i].s_x = ((int)result["s_x"]);
                UAVmove[i].s_y = ((int)result["s_y"]);
                UAVmove[i].s_z = ((int)result["s_z"]);
                UAVmove[i].target = new Vector3(UAVmove[i].s_x, UAVmove[i].s_y, UAVmove[i].s_z);

                await collection.UpdateManyAsync
                (
                    IHAfilter[i],
                    new BsonDocument
                    {
                        { "$set", new BsonDocument
                            {
                                { "a_z", Mathf.CeilToInt(UAVsensor[i].a_z) },
                                { "a_nz", Mathf.CeilToInt(UAVsensor[i].a_nz) },
                                { "a_x", Mathf.CeilToInt(UAVsensor[i].a_x) },
                                { "a_nx", Mathf.CeilToInt(UAVsensor[i].a_nx) },
                                { "a_y", Mathf.CeilToInt(UAVsensor[i].a_y) },
                                { "a_ny", Mathf.CeilToInt(UAVsensor[i].a_ny) },

                                { "e_z", Mathf.CeilToInt(UAVsensor[i].e_z) },
                                { "e_nz", Mathf.CeilToInt(UAVsensor[i].e_nz) },
                                { "e_x", Mathf.CeilToInt(UAVsensor[i].e_x) },
                                { "e_nx", Mathf.CeilToInt(UAVsensor[i].e_nx) },
                                { "e_y", Mathf.CeilToInt(UAVsensor[i].e_y) },
                                { "e_ny", Mathf.CeilToInt(UAVsensor[i].e_ny) }
                            }
                        }
                    }
                );
            
            
            }
            for (int i = 0; i < controlPanel.tankS; i++)
            {    
         
                //aracın gidecek konumlarını AL
                var result = await collectionIkas.Find(İKAfilter[i]).FirstOrDefaultAsync();
                IKAmove[i].s_x = ((int)result["s_x"]);
                IKAmove[i].s_y = ((int)result["s_y"]);
                IKAmove[i].s_z = ((int)result["s_z"]);
                IKAmove[i].target = new Vector3(IKAmove[i].s_x, IKAmove[i].s_y, IKAmove[i].s_z);
          
                 await collectionIkas.UpdateManyAsync
                (
                    İKAfilter[i],
                    new BsonDocument
                    {
                        { "$set", new BsonDocument
                            {
                                { "a_z", Mathf.CeilToInt(IKAsensor[i].a_z) },
                                { "a_nz", Mathf.CeilToInt(IKAsensor[i].a_nz) },
                                { "a_x", Mathf.CeilToInt(IKAsensor[i].a_x) },
                                { "a_nx", Mathf.CeilToInt(IKAsensor[i].a_nx) },

                                { "e_z", Mathf.CeilToInt(IKAsensor[i].e_z) },
                                { "e_nz", Mathf.CeilToInt(IKAsensor[i].e_nz) },
                                { "e_x", Mathf.CeilToInt(IKAsensor[i].e_x) },
                                { "e_nx", Mathf.CeilToInt(IKAsensor[i].e_nx) },
                            }
                        }
                    }
                );
            }
        }
    }
    */
}
