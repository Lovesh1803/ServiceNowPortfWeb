import React, { useState } from "react";
import "./CandidateDetails.css";

const CandidateDetails = ({ candidates }) => {
  const [filters, setFilters] = useState({});

  /**
   * @author Lovesh Singh.
   * @since 01-03-2025.
   * @param data data for extracting columns
   * @returns Array of columns
   * @description Extract unique keys (flattened for nested objects)
   */
  const extractColumns = (data) => {
    let columns = new Set();
    data.forEach((item) => {
      const traverse_column = (obj, prefix = "") => {
        Object.entries(obj).forEach(([key, value]) => {
          const newKey = prefix ? `${prefix} -> ${key}` : key;
          if (
            typeof value === "object" &&
            value !== null &&
            !Array.isArray(value)
          ) {
            traverse_column(value, newKey);
          } else {
            columns.add(newKey);
          }
        });
      };
      traverse_column(item);
    });
    return Array.from(columns);
  };

  const columns = extractColumns(candidates);

  /**
   * @author Lovesh Singh.
   * @since 01-03-2025.
   * @param column column value
   * @description Handle filter input changes
   */
  const handleFilterChange = (column, value) => {
    setFilters((prev) => ({ ...prev, [column]: value.toLowerCase() }));
  };

  /**
   * @author Lovesh Singh.
   * @since 01-03-2025.
   * @description Apply filters to the data
   */
  const filteredCandidates = candidates.filter((candidate) => {
    return Object.entries(filters).every(([column, value]) => {
      const keys = column.split(" -> ");
      let fieldValue = candidate;
      keys.forEach((key) => {
        if (fieldValue) fieldValue = fieldValue[key];
      });

      return fieldValue?.toString().toLowerCase().includes(value);
    });
  });

  return (
    <div className="candidates_container">
      <h2>Candidate List</h2>

      {/* Filter Inputs */}
      <div className="candidates_container__filters">
        <h3>Filters:</h3>
        {columns.map((col) => {
          const keys = col.split(" -> ");
          const placeholder = `Filter by ${keys[keys.length - 1]}`;

          return (
            <input
              key={col}
              type="text"
              placeholder={placeholder}
              onChange={(e) => handleFilterChange(col, e.target.value)}
              className="candidates_container__filter_input"
            />
          );
        })}
      </div>

      {/* Data Table */}
      <table
        border="1"
        cellPadding="8"
        cellSpacing="0"
        className="candidates_container__table"
      >
        <thead>
          <tr>
            {columns.map((col) => (
              <th key={col} className="candidates_container__table_heading">
                {col}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {filteredCandidates.map((candidate, index) => (
            <tr key={index}>
              {columns.map((col) => {
                const keys = col.split(" -> ");
                let value = candidate;
                keys.forEach((key) => {
                  if (value) value = value[key];
                });

                // Format arrays and default empty values
                if (Array.isArray(value)) value = value.join(", ");
                else if (value === undefined || value === null) value = "-";

                return <td key={col}>{value}</td>;
              })}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default CandidateDetails;
