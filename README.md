---

# HTTP2DNS - Encapsulamento de pacotes TCP em pacotes DNS

Bem-vindo ao projeto **HTTP2DNS**! 🎉

Este projeto é um exemplo prático para demonstrar como funcionam alguns aplicativos que fornecem acesso à internet gratuita encapsulando pacotes TCP em pacotes DNS. A técnica utilizada neste código é conhecida por "Tunneling DNS" e é uma forma de comunicação usada em redes que permitem tráfego DNS, mas restringem outros tipos de tráfego. 💻🌐

## 🚀 Objetivo do Projeto

O objetivo principal deste projeto é exemplificar o processo de encapsulamento de pacotes TCP dentro de pacotes DNS, técnica que muitos aplicativos utilizam para contornar restrições de acesso à internet. Ele pode ser usado para fins educacionais e para entendimento de como funcionam técnicas como **DNS Tunneling**. 🤓

> ⚠️ **Atenção**: Este projeto é apenas para fins educativos. O uso dessa técnica pode ser considerado uma violação de termos de serviço de algumas redes e provedores de internet. Use-o com responsabilidade! 😉

## 📑 Funcionalidades

- Encapsulamento de pacotes TCP em pacotes DNS
- Comunicação entre cliente e servidor através de pacotes DNS
- Exemplo prático de como funciona o "tunneling" de dados

## 📦 Estrutura do Projeto

```
http2dns/
│
├── client.py            # Script do cliente que envia pacotes TCP encapsulados em DNS
├── server.py            # Script do servidor que decapsula os pacotes DNS recebidos
├── README.md            # Este arquivo!
└── requirements.txt     # Dependências necessárias para rodar o projeto
```

## 🛠️ Como Rodar o Projeto

### Pré-requisitos

Antes de rodar o projeto, certifique-se de ter instalado:

- **Python 3.x** 🐍
- As dependências listadas no arquivo `requirements.txt`

### Instalação das Dependências

Instale as dependências necessárias rodando o comando:

```bash
pip install -r requirements.txt
```

### Como Executar

1. **Inicie o servidor**:

   Execute o script do servidor, que ficará aguardando pacotes DNS encapsulados:

   ```bash
   python server.py
   ```
  O servidor abrira a porta UDP 53

2. **Execute o cliente**:

   Em outro terminal, execute o script do cliente para começar a enviar pacotes TCP encapsulados:

   ```bash
   python client.py <IP SERVIDOR DNS> <DOMINIO>
   ```
   é necessario especificar o IP do servidor DNS e o dominio para fazer uma chamada HTTP
   ```bash
    python3 cliente.py 127.0.0.1 google.com
   ```

Agora o servidor e o cliente estarão se comunicando via pacotes DNS encapsulados. 🎉

## 🧠 Como Funciona?

Este projeto utiliza uma técnica conhecida como **DNS Tunneling**, que envolve encapsular pacotes TCP em pacotes DNS. Isso permite que dados sejam transmitidos através de redes que apenas permitem tráfego DNS. Muitos aplicativos que fornecem "internet gratuita" em redes restritas utilizam uma técnica semelhante.

Aqui está um resumo do fluxo:

1. O **cliente** encapsula os pacotes TCP dentro de pacotes DNS.
2. O pacote DNS encapsulado é enviado ao **servidor**, que está aguardando para recebê-los.
3. O **servidor** decapsula os pacotes DNS, recuperando o conteúdo original (pacotes TCP).

Essa técnica pode ser utilizada para contornar bloqueios ou restrições de rede, desde que o tráfego DNS seja permitido.

## 📚 Referências

- [DNS Tunneling - Explicação Técnica](https://en.wikipedia.org/wiki/DNS_tunneling)
- [RFC 1035 - Domain Names - Implementation and Specification](https://tools.ietf.org/html/rfc1035)



---
