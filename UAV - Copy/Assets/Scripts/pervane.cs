using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class pervane : MonoBehaviour
{

    void Start()
    {
        
    }

    void Update()
    {
        if (transform.position.y > 2)
        {
            transform.Rotate(0, 0, 20);
        }
        else
        {
            transform.Rotate(0, 0, 5);
        }

    }
}
