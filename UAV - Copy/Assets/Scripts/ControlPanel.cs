using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class ControlPanel : MonoBehaviour
{
    public int uavS,tankS;
    public GameObject uav,tank;
    public Vector3 uavSpawnPoint,tankSpawnPoint;


    public float x,y,z;

    public TMP_InputField uavSayisi,tankSayisi;





    void Start()
    {
        uavSpawnPoint = new Vector3(0,0,0);
        tankSpawnPoint = new Vector3(0,0,0);
    }

    void Update()
    {

    }

    public void StartButton()
    {   
        uavS = int.Parse(uavSayisi.text);
        tankS = int.Parse(tankSayisi.text);


        for (int i = 1; i < uavS+1; i++)    
        {
            //int sayac = 1;

            var clone = Instantiate(uav, uavSpawnPoint, Quaternion.identity);
            clone.name = "İHA" + i;

           /* if(sayac %2 == 0)
            {
                uavSpawnPoint.z += 90 * sayac;
            }
            else
            {
                uavSpawnPoint.z -= 90 * sayac;
            }
            */

           //sayac++;


        }
        for (int i = 1; i < tankS+1; i++)
        {
            var clone = Instantiate(tank, tankSpawnPoint, Quaternion.Euler(0, -90, 0));
            clone.name = "İKA" + i;
            //tankSpawnPoint.z += 20;
        }

    }
}
