// sendTx.js

import 'dotenv/config';
import { ethers } from 'ethers';

export async function sendBaseSepoliaEth(receiverAddress, amountInEth) {
    const rpcUrl = process.env.BASE_SEPOLIA_RPC_URL;
    const privateKey = process.env.BRUCE_WAYNE_PRIVATE_KEY;

    if (!rpcUrl || !privateKey) {
        const errorMsg = "❌ Missing BASE_SEPOLIA_RPC_URL or PRIVATE_KEY in your .env file.";
        console.error(errorMsg);
        return errorMsg;
    }

    try {
        const provider = new ethers.JsonRpcProvider(rpcUrl);
        const wallet = new ethers.Wallet(privateKey, provider);

        const tx = {
            to: receiverAddress,
            value: ethers.parseEther(amountInEth)
        };

        const txResponse = await wallet.sendTransaction(tx);
        const receipt = await txResponse.wait();

        const gasUsed = ethers.formatUnits(receipt.gasUsed, 'gwei');
        return `🎉 Transaction Confirmed!\n  - Hash: ${txResponse.hash}\n  - Block Number: ${receipt.blockNumber}\n  - Gas Used: ${gasUsed} gwei`;

    } catch (error) {
        console.error(error);
        return `❌ Transaction Failed: ${error.message}`;
    }
}
