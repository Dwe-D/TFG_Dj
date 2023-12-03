from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
import base64
from .models import NumerosModel

# Create your views here.
def tabla(request):

    return render(request, "tablas/tabla.html")

@csrf_exempt

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        try:
            # Parsear el JSON de la solicitud
            #data = json.loads(request.body)
            data = '''
            {
            "name": "as.up.data.forward",
            "time": "2023-12-03T23:26:23.824851850Z",
            "identifiers": [
                {
                "device_ids": {
                    "device_id": "eui-a8610a3130467613",
                    "application_ids": {
                    "application_id": "tfg-cx"
                    },
                    "dev_eui": "A8610A3130467613",
                    "join_eui": "0000000000000001",
                    "dev_addr": "260BB93E"
                }
                }
            ],
            "data": {
                "@type": "type.googleapis.com/ttn.lorawan.v3.ApplicationUp",
                "end_device_ids": {
                "device_id": "eui-a8610a3130467613",
                "application_ids": {
                    "application_id": "tfg-cx"
                },
                "dev_eui": "A8610A3130467613",
                "join_eui": "0000000000000001",
                "dev_addr": "260BB93E"
                },
                "correlation_ids": [
                "gs:uplink:01HGS027VSGJRWAG255NRAKQQD"
                ],
                "received_at": "2023-12-03T23:26:23.818237141Z",
                "uplink_message": {
                "session_key_id": "AYwyAOsgLN0yH3Y899rowg==",
                "f_port": 2,
                "f_cnt": 1,
                "frm_payload": "ABYAIQ==",
                "decoded_payload": {
                    "numero1": 22,
                    "numero2": 33
                },
                "rx_metadata": [
                    {
                    "gateway_ids": {
                        "gateway_id": "eui-58a0cbfffe804354",
                        "eui": "58A0CBFFFE804354"
                    },
                    "time": "2023-12-03T23:26:23.546581983Z",
                    "timestamp": 821777636,
                    "rssi": -78,
                    "channel_rssi": -78,
                    "snr": 10,
                    "uplink_token": "CiIKIAoUZXVpLTU4YTBjYmZmZmU4MDQzNTQSCFigy//+gENUEOSp7YcDGgwIn520qwYQ1KSoogIgoLWOrvWUAQ==",
                    "received_at": "2023-12-03T23:26:23.562702786Z"
                    }
                ],
                "settings": {
                    "data_rate": {
                    "lora": {
                        "bandwidth": 125000,
                        "spreading_factor": 7,
                        "coding_rate": "4/5"
                    }
                    },
                    "frequency": "867700000",
                    "timestamp": 821777636,
                    "time": "2023-12-03T23:26:23.546581983Z"
                },
                "received_at": "2023-12-03T23:26:23.609809424Z",
                "consumed_airtime": "0.051456s",
                "version_ids": {
                    "brand_id": "arduino",
                    "model_id": "mkr-wan-1310",
                    "hardware_version": "1.0",
                    "firmware_version": "1.2.3",
                    "band_id": "EU_863_870"
                },
                "network_ids": {
                    "net_id": "000013",
                    "ns_id": "EC656E0000000181",
                    "tenant_id": "ttn",
                    "cluster_id": "eu1",
                    "cluster_address": "eu1.cloud.thethings.network"
                }
                }
            },
            "correlation_ids": [
                "gs:uplink:01HGS027VSGJRWAG255NRAKQQD"
            ],
            "origin": "ip-10-100-7-165.eu-west-1.compute.internal",
            "context": {
                "tenant-id": "CgN0dG4="
            },
            "visibility": {
                "rights": [
                "RIGHT_APPLICATION_TRAFFIC_READ"
                ]
            },
            "unique_id": "01HGS0282GZQN1RF62Y750ETFC"
            }
            '''
            # Imprimir el JSON recibido
            #print("JSON recibido:", data)

            # Acceder a los valores de numero1 y numero2 dentro de decoded_payload
            numero1 = data['data']['uplink_message']['decoded_payload']['numero1']
            numero2 = data['data']['uplink_message']['decoded_payload']['numero2']
            # Print the values
            print("Numero1:", numero1)
            print("Numero2:", numero2)
            
            # Guardar en la base de datos
            mi_modelo = NumerosModel(numero1=numero1, numero2=numero2)
            mi_modelo.save()

            return JsonResponse({'mensaje': 'Datos guardados correctamente'})
        except Exception as e:
            return JsonResponse({'error': f'Error al procesar la solicitud: {str(e)}'}, status=500)
    else:
        return JsonResponse({'error': 'Solicitud no válida'}, status=400)

