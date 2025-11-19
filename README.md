```markdown
# Agentic Fitness Intelligence (AFI)

**Automated Market Insights & Product Recommendations for Fitness Brands**

---

## Overview

Agentic Fitness Intelligence (AFI) is an AI-powered project that automatically scrapes market data, analyzes trends, identifies competitor gaps, and recommends actionable products for fitness brands. It produces a **fully agentic weekly report** along with **visual dashboards** for easy interpretation.

This project leverages:

- **Web Scraping:** Flipkart and competitors (e.g., Decathlon)  
- **Google Trends:** Track popularity of fitness products  
- **Agentic AI (LLM):** Generate trend insights, competitor gaps, and product recommendations  
- **Data Processing:** Merge and clean multiple data sources  
- **Visualization:** Bar charts, horizontal rankings, and heatmaps for stakeholders  

---

## Features

1. **Trend Insights**  
   Analyze popularity of fitness products (e.g., dumbbells, yoga mats) over time.

2. **Competitor Gap Analysis**  
   Identify areas for improvement or differentiation based on market trends.

3. **Product Recommendations**  
   Rank products by priority score and suggest actionable strategies.

4. **Visualization Dashboard**  
   Automatically generate charts:
   - Trend scores with color-coded insights  
   - Competitor gap demand levels  
   - Priority-based product recommendations  
   - Heatmap combining trend and priority scores  

---

## Folder Structure

```

Agentic-Fitness-Intelligence/
│
├─ main.py                   # Runs the full agentic AI pipeline
├─ visualize_report.py        # Generates charts and dashboards
├─ data/
│   └─ processed/
│       └─ merged_dataset.csv
├─ outputs/                  # Weekly report + charts saved here
├─ src/
│   ├─ scraper/              # Flipkart, competitor, trends scrapers
│   ├─ processors/           # Data merging and cleaning
│   ├─ llm/                  # Trend analyzer, competitor gap, recommendations
│   └─ utils/                # Logger and helper functions
└─ venv_rrai/                # Virtual environment

````

---

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd Agentic-Fitness-Intelligence
````

2. Create a virtual environment and install dependencies:

```bash
python -m venv venv_rrai
venv_rrai\Scripts\activate  # Windows
pip install -r requirements.txt
```

---

## Usage

1. Run the main agentic AI pipeline:

```bash
python main.py
```

* Generates `weekly_report.txt` in `outputs/`

2. Generate visual dashboards:

```bash
python visualize_report.py
```

* Saves charts in `outputs/`

  * `trend_insights.png`
  * `competitor_gaps.png`
  * `product_recommendations.png`
  * `product_dashboard_heatmap.png`

3. Open the report and visualizations to review actionable insights.

---

## Customization

* **Keywords:** Update the list in `main.py`:

```python
keywords = ["yoga mat", "dumbbell", "shaker", "skipping rope"]
```

* **Add products:** Update LLM modules (`trend_analyzer.py`, `competitor_insight.py`, `product_recommender.py`) with new product keywords and recommendation strategies.

* **Data sources:** Add more competitors or e-commerce sites by creating new scrapers in `src/scraper/`.

---

## Future Enhancements

* Interactive dashboard using **Streamlit** or **Dash**
* Automatic daily or weekly trend updates
* Export visualizations and reports as **PDFs**
* Include price comparisons and competitor benchmarking

---

## License

MIT License

```

---

If you want, I can **also create a ready-to-use `requirements.txt`** that matches this project so anyone can install all dependencies in one go.  

Do you want me to do that next?
```
