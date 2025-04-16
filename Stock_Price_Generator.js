// Stock_Price_Generator.js
const fs = require('fs');
const rawData = [];
let currentPrice = 100; // 시작 가격
const volatility = 0.02; // 하루 변동성 (2%)


rawData.push('("2999-12-31", 100.00)');

// 3000년 1월 2일부터 3000년 12월 31일까지 데이터 생성
let currentDate = new Date(3000, 0, 2); //

for (let i = 1; i <= 365; i++) {
    const dateString = currentDate.toISOString().split('T')[0]; //
    const randomFactor = (Math.random() - 0.5) * 2 * volatility; // -2% ~ 2% (하루 변동성)민큼 랜덤 변동
    currentPrice *= (1 + randomFactor); // 변동성 반영
    rawData.push(`("${dateString}", ${currentPrice.toFixed(2)})`); // 변동 후 가격 기록
    currentDate.setDate(currentDate.getDate() + 1);
}

const fileContent = rawData.join(',\n');
const now = new Date();
const fileName = `stock_data_${now.toISOString().split('T')[0]}_${now.getHours()}-${now.getMinutes()}-${now.getSeconds()}.txt`;

fs.writeFileSync(fileName, fileContent);

console.log(`마지막 줄: ${rawData[rawData.length - 1]}`);
console.log(`${fileName} 파일에 데이터가 저장되었습니다.`);
