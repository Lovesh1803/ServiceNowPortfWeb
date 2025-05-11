export const getSampleData = () => {
  let sampleData = [];
  for (let i = 1; i <= 20; i++) {
    sampleData.push({
      name: `Candidate ${i}`,
      phone: `99999${i}000`,
      email: `candidate${i}@example.com`,
      CV_Insight: {
        totalExperience: Math.floor(Math.random() * 15) + 1, // Between 1-15 years
        relevantExperience: Math.floor(Math.random() * 10) + 1, // Between 1-10 years
        Qualification: "B.Tech in Information Technology",
        pedigree: [
          "IIT Mumbai",
          "NIT Trichy",
          "Anna University",
          "BITS Pilani",
        ][Math.floor(Math.random() * 4)],
        requiredSkills: [
          "React",
          "JavaScript",
          "Python",
          "Django",
          "Node.js",
        ].slice(0, Math.floor(Math.random() * 5) + 1),
        additionalSkills: [
          "Docker",
          "AWS",
          "GraphQL",
          "MongoDB",
          "Kubernetes",
        ].slice(0, Math.floor(Math.random() * 5) + 1),
      },
      Candidate_Insight: {
        salary: `₹${Math.floor(Math.random() * 30) + 5} LPA`, // ₹5-30 LPA
        noticePeriod: `${Math.floor(Math.random() * 3) + 1} month${
          Math.random() > 0.5 ? "s" : ""
        }`,
        location: [
          "Bangalore",
          "Hyderabad",
          "Delhi",
          "Chennai",
          "Mumbai",
          "Pune",
        ][Math.floor(Math.random() * 6)],
        workingMode: ["Remote", "Hybrid", "Onsite"][
          Math.floor(Math.random() * 3)
        ],
        probationPeriod: `${Math.floor(Math.random() * 6) + 1} months`,
        companyType: ["MNC", "Startup", "Mid-Sized Firm"][
          Math.floor(Math.random() * 3)
        ],
      },
      Other_info: {
        hasTwoWheeler: Math.random() > 0.5 ? "Yes" : "No", //
        hasWifi: Math.random() > 0.5 ? "Yes" : "No",
      },
    });
  }

  return sampleData;
};
