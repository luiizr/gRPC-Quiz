#!/bin/bash

echo "⚙️  Configurando servidor Node.js..."

# Instala as dependências do package.json
echo "📥 Instalando dependências npm..."
npm install

if [ $? -eq 0 ]; then
    echo "✅ Configuração do servidor concluída!"
    echo "🚀 Para executar o servidor, use: ./run-server.sh"
else
    echo "❌ Erro ao instalar dependências com npm!"
    exit 1
fi 