import React from "react";
import CandidateDetails from "./candidate/CandidateDetails";
import { getSampleData } from "./utils/utility";

const App = () => {
  return <CandidateDetails candidates={getSampleData()} />;
};

export default App;
