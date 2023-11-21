import React, { useEffect, useState } from "react";
import { myScore } from "../utiles/news";
import {
  LineChart,
  Line,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
} from "recharts";

import Graph from "../components/Graph";

// userData api 연결해서 받아올거
// const userData = [
//   { name: "j1", value: 2.9 },
//   { name: "j2", value: 5.2 },
//   { name: "j3", value: 12.5 },
//   { name: "j4", value: 15.6 },
//   { name: "j5", value: 6.1 },
//   { name: "j6", value: 1.2 },
//   { name: "j7", value: 3.5 },
//   { name: "j8", value: 4.3 },
//   { name: "j9", value: 57 },
// ];

interface Score {
  date: string;
  sum: number;
}

interface GraphData {
  name: string;
  value: number;
}

function ProfilePage() {
  const [userData, setUserData] = useState([]);
  const [allDate, setAllDate] = useState<any>();
  const [selectedDate, setSelectedDate] = useState<string | null>(null);
  const [graphData, setGraphData] = useState<GraphData[]>([]);

  const average = 237.9; // 평균값

  useEffect(() => {
    const fetchData = async () => {
      const result = await myScore("김동현");
      setAllDate(result.data.date);
      console.log(result.data.date["2023-11-21"]);
      const processedData: any = Object.entries(result.data.date).map(
        ([date, values]: any) => {
          const sum = Object.values(values).reduce(
            (a: any, b) => a + Number(b),
            0
          );
          return { date, sum };
        }
      );
      setUserData(processedData);
      console.log(processedData);
    };

    fetchData();
  }, []);

  const handleXAxisClick = (data: any) => {
    console.log(data?.activeLabel);
    setSelectedDate(data?.activeLabel);
  };

  useEffect(() => {
    if (selectedDate) {
      const selectedData = allDate[selectedDate];
      const processedData: GraphData[] = Object.entries(selectedData).map(
        ([name, value]) => ({
          name,
          value: Number(value),
        })
      );
      setGraphData(processedData);
    }
  }, [selectedDate, allDate]);

  return (
    <div>
      <div>프로필 페이지입니다. 날짜별 검사 종합지수가 보여요</div>
      {/* 평균 비교하는 차트 입니다. */}
      <LineChart
        width={500}
        height={300}
        data={userData}
        onClick={handleXAxisClick}
      >
        <Line type="monotone" dataKey="sum" stroke="#0b00e1" name="종합지수" />

        {/* 평균선임 */}
        <Line
          type="monotone"
          dataKey={() => average}
          stroke="#ef6b00"
          name="종합지수평균"
        />
        <CartesianGrid stroke="#ccc" />
        <XAxis dataKey="date" />
        <YAxis />
        <Tooltip />
      </LineChart>
      {selectedDate && (
        <>
          <div>선택된 날짜: {selectedDate}</div>
          <Graph userData={graphData} />
        </>
      )}
    </div>
  );
}

export default ProfilePage;
