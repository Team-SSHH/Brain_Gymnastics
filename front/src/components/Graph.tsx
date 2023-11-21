import React from "react";
import {
  LineChart,
  Line,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
} from "recharts";

interface Data {
  name: string;
  value: number;
}

interface GraphProps {
  userData: Data[];
}

const averageData: Data[] = [
  { name: "j1", value: 8.15 },
  { name: "j2", value: 5.5 },
  { name: "j3", value: 22 },
  { name: "j4", value: 11.1 },
  { name: "j5", value: 6.85 },
  { name: "j6", value: 2.95 },
  { name: "j7", value: 6.7 },
  { name: "j8", value: 1.75 },
  { name: "j9", value: 179 },
];

const Graph: React.FC<GraphProps> = ({ userData }) => {
  const formatXAxis = (data: string) => {
    return `${data}검사`;
  };
  const formatYAxis = (score: number) => {
    if (score === 0) {
      return "";
    }
    return `${score}점`;
  };

  return (
    <LineChart
      width={1000}
      height={300}
      data={averageData}
      margin={{ top: 5, right: 20, bottom: 5, left: 0 }}
    >
      <Line
        type="monotone"
        dataKey="value"
        stroke="#ff0000"
        fill="#ff0000"
        strokeWidth={5}
        name="평균점수"
      />
      <Line
        type="monotone"
        dataKey="value"
        stroke="#0b00e1"
        fill="#0b00e1"
        strokeWidth={5}
        name="나의점수"
        data={userData}
        className="text-lg"
      />
      <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
      <XAxis
        dataKey="name"
        stroke="#fffff"
        tickFormatter={formatXAxis}
        className="text-xl font-bold"
      />
      <YAxis
        domain={[0, 30]}
        allowDataOverflow={true}
        stroke="#fffff"
        tickFormatter={formatYAxis}
        className="text-xl font-bold"
      />
      <Tooltip contentStyle={{ fontSize: "28px" }} />
    </LineChart>
  );
};

export default Graph;
