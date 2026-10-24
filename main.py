# import requests


# url = "https://jsonplaceholder.typicode.com/posts/1"

# response = requests.get(url)
# dados = response.json()

# print(f'ID: {dados["id"]}')
# print(f'Título: {dados["title"]}')
# print(f'Conteúdo: {dados["body"]}')

# print(dados)
# print(dados["title"])
# print("Status:", response.status_code)
# print("Headers:", response.headers)
# print("Texto:", response.text)

# import requests

# url = "https://jsonplaceholder.typicode.com/posts"

# parametros = {
#     "userId": 1
# }

# response = requests.get(
#     url,
#     params=parametros
# )

# dados = response.json()

# for dado in dados:
#     print(f"ID: {dado['id']} - Título: {dado['title']}")


# import requests


# url = "https://jsonplaceholder.typicode.com/posts"

# novo_post = {
#     "userId": 1,
#     "title": "Estudando APIs",
#     "body": "Aprendendo POST com Python"
# }

# response = requests.post(
#     url,
#     json=novo_post
# )

# dados = response.json()

# print(response.status_code)
# print(dados)
# print(response.request.headers)
# print(response.request.body)


# import requests

# url = "https://jsonplaceholder.typicode.com/posts/999999"

# print(response.status_code)
# print(response.text)

# response.raise_for_status()

# print("Esta linha será executada?")


# import requests

# url = "https://jsonplaceholder.typicode.com/posts/999999"

# try:
#     # request
#     response = requests.get(
#         url,
#         timeout=5
#         )
#     # raise_for_status
#     response.raise_for_status()
#     # converter JSON
#     dados = response.json()
#     # imprimir dados
#     print(response.status_code)
#     print(dados)

# except requests.exceptions.HTTPError as erro:
#     print(f"Status: {erro.response.status_code}")
#     print(f"URL: {erro.response.url}")
#     print(f"Resposta: {erro.response.text}")


# except requests.exceptions.Timeout:
#     print("A API demorou demais para responder.")

# except requests.exceptions.ConnectionError:
#     print("Não foi possível conectar à API.")

# except requests.exceptions.RequestException:
#     print("Erro inesperado na requisição.")



# import requests

# url = "https://jsonplaceholder.typicode.com/posts/"

# token = "abc123xyz"

# headers = {
#     "Authorization": "Bearer " + token,
#     "Accept": "application/json"
# }

# try:
#     # request
#     response = requests.get(
#         url,
#         headers=headers,
#         timeout=5
#         )
#     # raise_for_status
#     response.raise_for_status()
#     # converter JSON
#     # dados = response.json()
#     # imprimir dados
#     print(response.status_code)
#     # print(dados)
#     print(response.request.headers)

# except requests.exceptions.HTTPError as erro:
#     print(f"Status: {erro.response.status_code}")
#     print(f"URL: {erro.response.url}")
#     print(f"Resposta: {erro.response.text}")


# except requests.exceptions.Timeout:
#     print("A API demorou demais para responder.")

# except requests.exceptions.ConnectionError:
#     print("Não foi possível conectar à API.")

# except requests.exceptions.RequestException:
#     print("Erro inesperado na requisição.")



# import requests

# url = "https://jsonplaceholder.typicode.com/posts/999999"

# token = "abc123xyz"

# headers = {
#     "Authorization": "Bearer " + token,
#     "Accept": "application/json"
# }


# def tratar_erro_http(status: int) -> None:
#     if status == 401:
#         print(f"Status: {status}. Credencial inválida ou expirada.")

#     elif status == 403:
#         print(f"Status: {status}. Sem permissão para acessar este recurso.")

#     elif status == 404:
#         print(f"Status: {status}. Recurso não encontrado.")

#     elif status == 429:
#         print(f"Status: {status}. Limite de requisições excedido.")

#     elif status in (500, 502, 503, 504):
#         print(f"Status: {status}. Erro temporário no servidor.")

#     else:
#         print(f"Erro HTTP: {status}")


# try:
#     # request
#     response = requests.get(
#         url,
#         headers=headers,
#         timeout=5
#         )
#     # raise_for_status
#     response.raise_for_status()
#     # converter JSON
#     dados = response.json()
#     # imprimir dados
#     print(response.status_code)
#     print(dados)

# except requests.exceptions.HTTPError as erro:

#     status = erro.response.status_code
#     tratar_erro_http(status)

# except requests.exceptions.Timeout:
#     print("A API demorou demais para responder.")

# except requests.exceptions.ConnectionError:
#     print("Não foi possível conectar à API.")

# except requests.exceptions.RequestException:
#     print("Erro inesperado na requisição.")



import requests
import time


def tratar_erro_http(status: int) -> None:
    if status == 401:
        print(f"Status: {status}. Credencial inválida ou expirada.")

    elif status == 403:
        print(f"Status: {status}. Sem permissão para acessar este recurso.")

    elif status == 404:
        print(f"Status: {status}. Recurso não encontrado.")

    elif status == 429:
        print(f"Status: {status}. Limite de requisições excedido.")

    else:
        print(f"Erro HTTP: {status}")


def aguardar_retry(tentativa: int) -> None:
    espera = 2 ** (tentativa - 1)
    print(f"Nova tentativa em {espera} segundo(s)...")
    time.sleep(espera)


MAX_TENTATIVAS = 3


def buscar_com_retry(url: str) -> dict | list | None:

    for tentativa in range(1, MAX_TENTATIVAS + 1):
        print(f"Tentativa {tentativa}/{MAX_TENTATIVAS}")

        try:
            response = requests.get(
                url,
                timeout=5
                )

            response.raise_for_status()

            dados = response.json()
            return dados

        except requests.exceptions.HTTPError as erro:

            status = erro.response.status_code

            if status == 429:

                retry_after = erro.response.headers.get("Retry-After")

                if retry_after is not None:

                    if tentativa == MAX_TENTATIVAS:
                        print(f"Status: {status}. Máximo de tentativas atingido.")
                        return None
                    
                    else:
                        espera = int(retry_after)
                        print(f"Limite excedido. Nova tentativa em {espera} segundos.")
                        time.sleep(espera)
                        continue

                else:
                    if tentativa == MAX_TENTATIVAS:
                        print("Máximo de tentativas atingido.")
                        return None

                    aguardar_retry(tentativa)
                    continue


            elif status in (500, 502, 503, 504):
                if tentativa == MAX_TENTATIVAS:
                    print("Máximo de tentativas atingido.")
                    return None

                aguardar_retry(tentativa)
                continue
            else:
                tratar_erro_http(status)
                return None

        except requests.exceptions.Timeout:
            print("A API demorou demais para responder.")

            if tentativa == MAX_TENTATIVAS:
                print("Máximo de tentativas atingido.")
                return None

            aguardar_retry(tentativa)
            continue

        except requests.exceptions.ConnectionError:
            print("Não foi possível conectar à API.")

            if tentativa == MAX_TENTATIVAS:
                print("Máximo de tentativas atingido.")
                return None

            aguardar_retry(tentativa)
            continue

        except requests.exceptions.RequestException:
            print("Erro inesperado na requisição.")
            return None


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts/1"
    resposta = buscar_com_retry(url)
    print(resposta)
