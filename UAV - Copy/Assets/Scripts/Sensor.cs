using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;


public class Sensor : MonoBehaviour
{
    //public TextMeshProUGUI sagMesafeText, solMesafeText, onMesafeText, arkaMesafeText, yukariMesafeText, asagiMesafeText, sagEngelMesafeText, solEngelMesafeText, onEngelMesafeText, arkaEngelMesafeText, yukariEngelMesafeText, asagiEngelMesafeText;
    //public TextMeshProUGUI enKucukText, enKucukEngelText;
    public float maxDistance = 30;
    public float enKucuk, enKucukEngel;
    public int a_nx, a_x, a_z, a_nz, a_y, a_ny , e_nx, e_x, e_z, e_nz, e_y, e_ny;
    public float[] mesafeler;
    public float[] engelMesafeler;
    public string enKucukYon, enKucukEngelYon;




    void Start()
    {
        
    }

    void Update()
    {   
        enKucuk = 8888;  // bunu yazıncaanlık olarak listedekilerden gösteriyor enküçükte twakılı kalmıyor ama bu doğru bir yol mu bilmiyorum.
        enKucukEngel= 8888;
        mesafeler = new float[6]{a_nx, a_x, a_z, a_nz, a_y, a_ny};
        engelMesafeler = new float[6]{e_nx, e_x, e_z, e_nz, e_y, e_ny};

        if(a_nx == a_x && a_nx == a_z && a_nx == a_nz && a_nx == a_y && a_nx == a_ny)
        {
            //enKucukText.text = "Temas Yok";
            enKucukYon = "Temas Yok";
        }
        else
        {
            for (int i = 0; i < mesafeler.Length; i++)
            {
                if (mesafeler[i] < enKucuk)
                {
                    enKucuk = mesafeler[i];

                    if (mesafeler[i] == a_z)
                    {
                        enKucukYon = "Sag";
                    }
                    else if (mesafeler[i] == a_nz)
                    {
                        enKucukYon = "Sol";
                    }
                    else if (mesafeler[i] == a_x)
                    {
                        enKucukYon = "On";
                    }
                    else if (mesafeler[i] == a_nx)
                    {
                        enKucukYon = "Arka";
                    }
                    else if (mesafeler[i] == a_y)
                    {
                        enKucukYon = "Yukari";
                    }
                    else if (mesafeler[i] == a_ny)
                    {
                        enKucukYon = "Asagi";
                    }
                    //enKucukText.text = enKucukYon + "   " + enKucuk.ToString("F2") + " M";
                }  
                
            } 
        }
        if(e_nx == e_x && e_nx == e_z && e_nx == e_nz && e_nx == e_y && e_nx == e_ny)
        {
            //enKucukEngelText.text = "Engel Yok";
            enKucukEngelYon = "Engel Yok";
        }
        else
        {
            for (int i = 0; i < engelMesafeler.Length; i++)
            {
                if (engelMesafeler[i] < enKucukEngel)
                {
                    enKucukEngel = engelMesafeler[i];

                    if (engelMesafeler[i] == e_z)
                    {
                        enKucukEngelYon = "Sag";
                    }
                    else if (engelMesafeler[i] == e_nz)
                    {
                        enKucukEngelYon = "Sol";
                    }
                    else if (engelMesafeler[i] == e_x)
                    {
                        enKucukEngelYon = "On";
                    }
                    else if (engelMesafeler[i] == e_nx)
                    {
                        enKucukEngelYon = "Arka";
                    }
                    else if (engelMesafeler[i] == e_y)
                    {
                        enKucukEngelYon = "Yukari";
                    }
                    else if (engelMesafeler[i] == e_ny)
                    {
                        enKucukEngelYon = "Asagi";
                    }
                    //enKucukEngelText.text = enKucukEngelYon + "   " + enKucukEngel.ToString("F2") + " M";
                }
            }
        }
        
    }



    #region Gizmos //Yazdirma//Çizdirme//Sersör Mesafeleri
    void OnDrawGizmos()
    {
        RaycastHit hit;

        if (Physics.BoxCast(transform.position, transform.lossyScale * 2, Vector3.left, out hit, Quaternion.identity, maxDistance))
        {
            Gizmos.color = Color.red;
            Gizmos.DrawRay(transform.position, Vector3.left * hit.distance);
            Gizmos.DrawWireCube(transform.position + Vector3.left * hit.distance, transform.lossyScale * 4);

            if (hit.transform.tag=="UAV" || hit.transform.tag =="TANK")
            {
                a_nx = Mathf.CeilToInt(hit.distance) + 2;  // Mesafe yesik karenin yani boxcastin sıbırlarında çıktığından itibaren ölçülüyor. yani 0 dan değil boxcast 5 ise 10 dan başlayarak ölçülüyor. 10 da uçağı içine aldığı için büyük oranda. yani ölçüm uçağına sınırlarında itibaren oluyor.
                e_nx = 999;                        //Yani uçak 0 0 0 daysa ve onden ölçüyorsa (ön Z) 0 0 10 dan 0 ile olçmeye başlayıp 0 0 40 a kadar ölçecek ben 30 ayarladığım için. (10 olunca 8 ölçüyor o da olsun.. 12 den başlıyormuş hesaplamaya gerisini normal hesaplıyor.)
            }
            else if(hit.transform.tag=="ENGEL")
            {
                e_nx = Mathf.CeilToInt(hit.distance) + 2;
                a_nx = 999;  
            }
        }

        else
        {
            Gizmos.color = Color.green;
            Gizmos.DrawRay(transform.position, Vector3.left * (maxDistance + 4));
            Gizmos.DrawWireCube(transform.position + Vector3.left * hit.distance, transform.lossyScale * 4);

            a_nx = 999;    
            e_nx = 999;

        } 
       if (Physics.BoxCast(transform.position, transform.lossyScale * 2, Vector3.right, out hit, Quaternion.identity, maxDistance))
        {
            Gizmos.color = Color.red;
            Gizmos.DrawRay(transform.position, Vector3.right * hit.distance);
            Gizmos.DrawWireCube(transform.position + Vector3.right * hit.distance, transform.lossyScale * 4);
            if (hit.transform.tag=="UAV" || hit.transform.tag =="TANK")
            {
                a_x = Mathf.CeilToInt(hit.distance) + 2;
                e_x = 999;
            }
            else if(hit.transform.tag=="ENGEL")
            {
                e_x = Mathf.CeilToInt(hit.distance) + 2;
                a_x = 999;
            }
        }

        else
        {
            Gizmos.color = Color.green;
            Gizmos.DrawRay(transform.position, Vector3.right * (maxDistance + 4));
            Gizmos.DrawWireCube(transform.position + Vector3.right * hit.distance, transform.lossyScale * 4);

            a_x = 999;
            e_x = 999;
        }
        if (Physics.BoxCast(transform.position, transform.lossyScale * 2, Vector3.forward, out hit, Quaternion.identity, maxDistance))
        {
            Gizmos.color = Color.red;
            Gizmos.DrawRay(transform.position, Vector3.forward * hit.distance);
            Gizmos.DrawWireCube(transform.position + Vector3.forward * hit.distance, transform.lossyScale * 4);

            if (hit.transform.tag=="UAV" || hit.transform.tag =="TANK")
            {
                a_nz = Mathf.CeilToInt(hit.distance) + 2;
                e_nz = 999;
            }
            else if(hit.transform.tag=="ENGEL")
            {
                e_nz = Mathf.CeilToInt(hit.distance) + 2;
                a_nz = 999;
            }
        }

        else
        {
            Gizmos.color = Color.green;
            Gizmos.DrawRay(transform.position, Vector3.forward * (maxDistance + 4));
            Gizmos.DrawWireCube(transform.position + Vector3.forward * hit.distance, transform.lossyScale * 4);

            a_nz = 999;
            e_nz = 999;
        }
        if (Physics.BoxCast(transform.position, transform.lossyScale * 2, Vector3.back, out hit, Quaternion.identity, maxDistance))
        {
            Gizmos.color = Color.red;
            Gizmos.DrawRay(transform.position, Vector3.back * hit.distance);
            Gizmos.DrawWireCube(transform.position + Vector3.back * hit.distance, transform.lossyScale * 4);

            if (hit.transform.tag=="UAV" || hit.transform.tag =="TANK")
            {
                a_z = Mathf.CeilToInt(hit.distance) + 2;
                e_z = 999;
            }
            else if(hit.transform.tag=="ENGEL")
            {
                e_z = Mathf.CeilToInt(hit.distance) + 2;
                a_z = 999;
            }
        }
        else
        {
            Gizmos.color = Color.green;
            Gizmos.DrawRay(transform.position, Vector3.back * (maxDistance + 4));
            Gizmos.DrawWireCube(transform.position + Vector3.back * hit.distance, transform.lossyScale * 4);

            a_z = 999;
            e_z = 999;
        }
        if (Physics.BoxCast(transform.position, transform.lossyScale * 2, Vector3.up, out hit, Quaternion.identity, maxDistance))
        {
            Gizmos.color = Color.red;
            Gizmos.DrawRay(transform.position, Vector3.up * hit.distance);
            Gizmos.DrawWireCube(transform.position + Vector3.up * hit.distance, transform.lossyScale * 4);

            if (hit.transform.tag=="UAV" || hit.transform.tag =="TANK")
            {
                a_y = Mathf.CeilToInt(hit.distance) + 2;
                e_y = 999;
            }
            else if(hit.transform.tag=="ENGEL")
            {
                e_y = Mathf.CeilToInt(hit.distance) + 2;
                a_y = 999;
            }
        }
        else
        {
            Gizmos.color = Color.green;
            Gizmos.DrawRay(transform.position, Vector3.up * (maxDistance + 4));
            Gizmos.DrawWireCube(transform.position + Vector3.up * hit.distance, transform.lossyScale * 4);

            a_y = 999;
            e_y = 999;
        }
        if (Physics.BoxCast(transform.position, transform.lossyScale * 2, -Vector3.up, out hit, Quaternion.identity, maxDistance))
        {
            Gizmos.color = Color.red;
            Gizmos.DrawRay(transform.position, -Vector3.up * hit.distance);
            Gizmos.DrawWireCube(transform.position - Vector3.up * hit.distance, transform.lossyScale * 4);

           if (hit.transform.tag=="UAV" || hit.transform.tag =="TANK")
            {
                a_ny = Mathf.CeilToInt(hit.distance) + 2;
                e_ny = 999;
            }
            else if(hit.transform.tag=="ENGEL")
            {
                e_ny = Mathf.CeilToInt(hit.distance) + 2;
                a_ny = 999;
            }
        }
        else
        {
            Gizmos.color = Color.green;
            Gizmos.DrawRay(transform.position, -Vector3.up * (maxDistance + 4));
            Gizmos.DrawWireCube(transform.position - Vector3.up * hit.distance, transform.lossyScale * 4);

            a_ny = 999;
            e_ny = 999;
        }
        //sagMesafeText.text = "sag: " + a_z.ToString("F0");
        //solMesafeText.text = "sol: " + a_nz.ToString("F0");
        //onMesafeText.text = "on: " + a_x.ToString("F0");
        //arkaMesafeText.text = "arka: " + a_nx.ToString("F0");
        //yukariMesafeText.text = "yukari: " + a_y.ToString("F0");
        //asagiMesafeText.text = "asagi: " + a_ny.ToString("F0");

        //sagEngelMesafeText.text = "sag: " + e_z.ToString("F0");
        //solEngelMesafeText.text = "sol: " + e_nz.ToString("F0");
        //onEngelMesafeText.text = "on: " + e_x.ToString("F0");
        //arkaEngelMesafeText.text = "arka: " + e_nx.ToString("F0");
        //yukariEngelMesafeText.text = "yukari: " + e_y.ToString("F0");
        //asagiEngelMesafeText.text = "asagi: " + e_ny.ToString("F0");
    }
    #endregion
    
    
}
