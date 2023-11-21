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
import BackBtn from "../components/ui/backBtn";
import TitleBtn from "../components/ui/titleBtn";

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

  const formatXAxis = (date: string) => {
    return `${date.slice(5, 7)}월 ${date.slice(8, 11)}일`;
  };
  const formatYAxis = (score: number) => {
    if (score === 0) {
      return "";
    }
    return `${score}점`;
  };

  return (
    <div>
      <div className="flex items-center">
        <BackBtn />
        <TitleBtn name="날짜별 검사 종합지수" />
      </div>
      <p className="text-center text-2xl">
        날짜를 클릭하면 세부 점수를 알 수 있어요!
        <span className="bg-[#0b00e1] text-white ml-5 px-1 rounded-full">
          나
        </span>
        <span className="bg-[#ff0000] text-white ml-5 px-1 rounded-full">
          평균
        </span>
      </p>
      <div className="mt-12 flex flex-col items-center justify-center h-full ">
        {/* 평균 비교하는 차트 입니다. */}
        <LineChart
          width={1000}
          height={300}
          data={userData}
          onClick={handleXAxisClick}
        >
          <Line
            type="monotone"
            dataKey="sum"
            stroke="#0b00e1"
            fill="#0b00e1"
            strokeWidth={5}
            name="내 종합지수"
            className="text-lg"
          />

          {/* 평균선임 */}
          <Line
            type="monotone"
            dataKey={() => average}
            stroke="#ff0000"
            fill="#ff0000"
            strokeWidth={5}
            name="내 나이대 종합지수 평균"
          />
          <CartesianGrid strokeDasharray="5 5" />
          <XAxis
            dataKey="date"
            stroke="#fffff"
            tickFormatter={formatXAxis}
            className="text-xl font-bold"
          />
          <YAxis
            stroke="#fffff"
            className="text-xl font-bold"
            tickFormatter={formatYAxis}
          />
          <Tooltip contentStyle={{ fontSize: "28px" }} />
        </LineChart>
        {selectedDate && (
          <div className="mt-10">
            <div className="font-bold text-3xl text-center">
              선택된 날짜: {selectedDate}
            </div>
            <div className="mt-10">
              <Graph userData={graphData} />
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default ProfilePage;
