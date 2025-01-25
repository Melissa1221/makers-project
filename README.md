# Makers Tech ChatBot Project

## Project Overview
This project is designed to assist a technology e-commerce company, **Makers Tech**, by developing a ChatBot capable of providing real-time inventory updates, product details, and pricing information. The ChatBot will offer a user-friendly graphical interface for personalized interaction.

In addition to the main functionality, optional features include a product recommendation system and an administrative dashboard for inventory metrics.

---

## Features

### Core Feature
- **ChatBot:**
  - Respond to user queries regarding inventory, features, and pricing in real-time.
  - Provide a personalized conversational experience.

### Optional Features
- **Product Recommendation System:**
  - Categorize products as "Highly Recommended," "Recommended," or "Not Recommended" based on user preferences.
  - Display recommendations when users log in.
- **Admin Dashboard:**
  - Visualize stock metrics through interactive charts and tables.
  - Access data such as total inventory, low-stock products, and sales trends.

---

## Technologies Used
- **Backend:** FastAPI, LangChain, SQLAlchemy
- **Frontend:**  React
- **Database:** PostgreSQL
- **Visualization:** Chart.js or D3.js (for dashboard metrics)
- **Authentication:** JWT-based authentication for secure user sessions

---

## Project Structure
```plaintext
app/
├── routers/      # API endpoints
├── models/       # Database models
├── schemas/      # Pydantic schemas for data validation
├── services/     # Core application logic
└── main.py       # Entry point for the FastAPI app
```

---

## Implementation Steps

### 1. Planificación y Análisis
1. **Revisión del requerimiento:**
   - Confirm functionalities for ChatBot, recommendation system, and dashboard.
2. **Elección de tecnologías:**
   - Select tools such as FastAPI, LangChain, and PostgreSQL.
3. **Diseño del sistema:**
   - Develop architecture and interaction diagrams.
4. **Definición de métricas:**
   - Determine dashboard metrics and visualization formats.

### 2. Desarrollo del ChatBot
1. **Diseño de la interfaz gráfica:**
   - Create a user-friendly interface with React.
2. **Lógica de inventario:**
   - Implement a database for predefined inventory.
3. **Integración de IA:**
   - Use LangChain for personalized ChatBot responses.
4. **Pruebas unitarias:**
   - Test the ChatBot for accuracy and performance.

### 3. Sistema de Recomendación
1. **Perfil del usuario:**
   - Capture preferences through explicit inputs or history.
2. **Algoritmo de recomendación:**
   - Implement collaborative filtering or content-based filtering.
3. **Clasificación de productos:**
   - Categorize products based on recommendations.
4. **Integración con la interfaz:**
   - Display recommendations in the user interface.

### 4. Dashboard para Administradores
1. **Diseño del dashboard:**
   - Define charts and tables for metrics.
2. **Lógica de backend:**
   - Build endpoints for fetching and processing metrics.
3. **Visualización de datos:**
   - Use Chart.js or D3.js for interactive visualizations.
4. **Pruebas de visualización:**
   - Ensure accurate and dynamic display of metrics.

### 5. Video Pitch y Presentación
1. **Preparación del pitch:**
   - Script and rehearse a presentation highlighting the project's benefits.
2. **Grabación del demo:**
   - Demonstrate the ChatBot, recommendation system, and dashboard.
3. **Edición del video:**
   - Ensure clarity and polish within a 5-minute limit.

### 6. Entrega Final
1. **Preparación del repositorio:**
   - Upload the code to GitHub/GitLab with clear documentation.
2. **Texto individual:**
   - Team members write 200-word summaries explaining the project's value.
3. **Revisión final:**
   - Verify compliance with all requirements.

---

## How to Run

### Prerequisites
1. Python 3.9+
2. Node.js 14+
3. PostgreSQL database
4. Virtual environment tools (e.g., `venv`, `conda`)

### Backend Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```
3. Configure the database connection in `database.py`.
4. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ```

### Frontend Setup
1. Navigate to the frontend folder:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```

---

## Development Setup

### Prerequisites
1. Python 3.9+
2. Poetry (Python package manager)
3. Git

### Initial Setup

1. Install Poetry (if not already installed):
   ```bash
   # Windows (PowerShell)
   (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

   # Unix/MacOS
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Clone and setup the project:
   ```bash
   # Clone the repository
   git clone <repository-url>
   cd makers-tech-chatbot

   # Install dependencies using Poetry
   poetry install

   # Activate the virtual environment
   poetry shell
   ```

3. Setup pre-commit hooks:
   ```bash
   # Install pre-commit hooks
   poetry run pre-commit install
   ```

### Development Workflow

1. **Code Formatting**:
   - Black formatter is automatically run on commit via pre-commit hooks
   - To manually format code:
     ```bash
     poetry run black .
     ```

2. **Running Tests**:
   ```bash
   poetry run pytest
   ```

3. **Running the Application**:
   ```bash
   poetry run uvicorn app.main:app --reload
   ```

4. **Adding New Dependencies**:
   ```bash
   # Add a production dependency
   poetry add package-name

   # Add a development dependency
   poetry add --group dev package-name
   ```

### Code Quality Tools

1. **Black** (Code Formatter):
   - Automatically formats code to follow a consistent style
   - Configuration in `pyproject.toml`
   - Run manually: `poetry run black .`

2. **Flake8** (Linter):
   - Checks for style and potential errors
   - Configuration in `.flake8`
   - Run manually: `poetry run flake8`

3. **Pre-commit**:
   - Runs checks before each commit
   - Configuration in `.pre-commit-config.yaml`
   - Run manually on all files: `poetry run pre-commit run --all-files`

### Best Practices

1. Always activate the virtual environment:
   ```bash
   poetry shell
   ```

2. Keep dependencies updated:
   ```bash
   poetry update
   ```

3. Format code before committing:
   ```bash
   poetry run black .
   ```

4. Run tests before pushing:
   ```bash
   poetry run pytest
   ```

---

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to your fork and submit a pull request.

---

## License
This project is licensed under the MIT License.
