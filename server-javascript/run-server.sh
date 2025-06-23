#!/bin/bash

echo "🚀 Iniciando servidor Node.js gRPC Quiz..."

# Verifica se as dependências foram instaladas
if [ ! -d "node_modules" ]; then
    echo "❌ Dependências não encontradas!"
    echo "🔧 Execute primeiro: ./setup.sh"
    exit 1
fi

# Executa o servidor
node quiz_server.js 