function detectAnomalies(data) {
  const feature1Values = data.map((row) => parseFloat(row.feature1));
  const mean = feature1Values.reduce((a, b) => a + b) / feature1Values.length;
  const stdDev = Math.sqrt(
    feature1Values.map((x) => Math.pow(x - mean, 2)).reduce((a, b) => a + b) /
      feature1Values.length
  );

  const anomalies = data.filter((row) => {
    const zScore = (parseFloat(row.feature1) - mean) / stdDev;
    return Math.abs(zScore) > 3; // Customize threshold
  });

  console.log("Anomalies Detected:", anomalies);
}
