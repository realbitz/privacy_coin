class Block {
    constructor(data, previousHash) {
        this.timestamp = new Date().getTime();
        this.data = data;
        this.previousHash = previousHash;
        this.hash = this.calculateHash();
    }

    calculateHash() {
        return sha256(this.timestamp + JSON.stringify(this.data) + this.previousHash);
    }
}

class Blockchain {
    constructor() {
        this.chain = [this.createGenesisBlock()];
    }

    createGenesisBlock() {
        return new Block("Genesis Block", "0");
    }

    getLatestBlock() {
        return this.chain[this.chain.length - 1];
    }

    addBlock(data) {
        let newBlock = new Block(data, this.getLatestBlock().hash);
        this.chain.push(newBlock);
    }

    isChainValid() {
        for (let i = 1; i < this.chain.length; i++) {
            const currentBlock = this.chain[i];
            const previousBlock = this.chain[i - 1];

            if (currentBlock.hash !== currentBlock.calculateHash()) {
                return false;
            }

            if (currentBlock.previousHash !== previousBlock.hash) {
                return false;
            }
        }

        return true;
    }
}

let blockchain = new Blockchain();

function addBlock() {
    let data = document.getElementById("data").value;
    blockchain.addBlock(data);
    document.getElementById("chain").innerHTML = JSON.stringify(blockchain.chain, null, 2);
}

function validateChain() {
    let isValid = blockchain.isChainValid();
    document.getElementById("isValid").innerHTML = isValid;
}