# SpendLess - Proactive Financial Assistant

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technology Stack](#technology-stack)
4. [Project Structure](#project-structure)
5. [Installation & Setup](#installation--setup)
6. [Configuration](#configuration)
7. [API Documentation](#api-documentation)
8. [AI/ML Services](#aiml-services)
9. [Database Schema](#database-schema)
10. [Usage Examples](#usage-examples)
11. [Development](#development)
12. [Testing](#testing)
13. [Deployment](#deployment)
14. [Contributing](#contributing)
15. [License](#license)
16. [Contact](#contact)

## Project Overview

**SpendLess** is a comprehensive proactive financial assistant that leverages advanced AI and machine learning technologies to provide intelligent banking solutions and financial predictions. Built as a modern banking application, SpendLess combines traditional banking features with cutting-edge predictive analytics to help users make informed financial decisions.

### What SpendLess Does

SpendLess serves as a complete banking ecosystem that offers:

- **Multi-Bank Account Management**: Seamlessly manage accounts across multiple banks with unified dashboard views
- **AI-Powered Financial Predictions**: Advanced machine learning models predict future expenses, income, and account balances
- **Intelligent Transaction Categorization**: Automatic categorization of transactions using AI clustering techniques
- **Proactive Notifications**: Smart alerts for insufficient balance, upcoming payments, and financial insights
- **Interactive Financial Chatbot**: Natural language interface for financial queries and assistance
- **Comprehensive Dashboard**: Real-time financial overview with analytics and insights
- **Todo & Reminder System**: Financial task management with automated reminders

### Problem It Solves

Traditional banking applications provide basic transaction history and account management, but lack intelligent insights and predictive capabilities. SpendLess addresses key pain points:

- **Reactive Financial Management**: Users often discover financial issues after they occur
- **Lack of Predictive Insights**: No visibility into future financial trends or potential problems
- **Fragmented Banking Experience**: Managing multiple bank accounts across different platforms
- **Limited Financial Intelligence**: Basic transaction categorization without meaningful insights
- **Poor Financial Planning**: No proactive assistance for financial decision-making

### Target Audience

- **Individual Users**: Personal banking customers seeking intelligent financial management
- **Small Business Owners**: Entrepreneurs needing comprehensive financial oversight
- **Financial Advisors**: Professionals requiring advanced analytics for client management
- **Tech-Savvy Consumers**: Users who appreciate AI-driven financial insights

### Key Value Propositions

1. **Predictive Financial Intelligence**: Advanced N-BEATS and TFT models provide accurate future financial predictions
2. **Proactive Financial Management**: Early warning systems prevent financial issues before they occur
3. **Unified Banking Experience**: Single platform for managing multiple bank accounts and financial data
4. **AI-Driven Insights**: Machine learning algorithms provide personalized financial recommendations
5. **Real-Time Notifications**: Instant alerts and updates via WebSocket connections
6. **Natural Language Interface**: Conversational AI for intuitive financial interactions
7. **Comprehensive Analytics**: Detailed financial reports and trend analysis
8. **Secure & Scalable**: Enterprise-grade security with MongoDB and modern authentication

## Features

SpendLess offers a comprehensive suite of banking and financial management features powered by advanced AI and machine learning technologies.

### User Authentication & Management
- **Secure Login System**: JWT-based authentication with token refresh capabilities
- **User Registration**: Complete sign-up process with OTP verification
- **Profile Management**: Update personal information, profile pictures, and contact details
- **Password Management**: Secure password change and forgot password functionality
- **Phone Number Verification**: OTP-based phone number validation and updates

### Bank Account Management
- **Multi-Bank Support**: Manage accounts across multiple banks from a single platform
- **Account Addition**: Secure bank account linking with OTP verification
- **Account Removal**: Safe account disconnection with confirmation
- **Account Details**: Comprehensive view of all linked accounts
- **Bank Directory**: Access to supported banks with rates and information
- **Credit Account Management**: Special handling for credit cards and loan accounts

### Dashboard & Analytics
- **Unified Dashboard**: Real-time overview of all financial accounts
- **Account-Specific Views**: Detailed analytics for individual accounts
- **Time Period Analysis**: Custom date range financial summaries
- **Credit Summary**: Comprehensive credit account analytics
- **Financial Health Metrics**: Key performance indicators and trends
- **Surplus Account Detection**: Identify accounts with excess funds

### Transaction Management
- **Transaction History**: Complete transaction records with filtering options
- **Advanced Filtering**: Filter by date range, amount range, and specific values
- **Account-Specific Transactions**: View transactions for individual accounts
- **Transaction Search**: Find specific transactions quickly
- **Receipt Management**: Store and manage transaction receipts

### AI-Powered Transaction Categorization
- **Automatic Categorization**: AI-driven transaction classification
- **Category Management**: Create, edit, and manage transaction categories
- **Bulk Categorization**: Process multiple transactions simultaneously
- **Category Customization**: Rename and modify categories as needed
- **Transaction Re-categorization**: Move transactions between categories
- **Smart Clustering**: Advanced ML algorithms for pattern recognition

### Financial Predictions & AI Analytics
- **Balance Predictions**: Future account balance forecasting using N-BEATS models
- **Expense Predictions**: AI-powered expense forecasting with uncertainty metrics
- **Income Predictions**: Future income prediction with confidence intervals
- **Category-wise Predictions**: Detailed predictions by transaction categories
- **TFT (Temporal Fusion Transformer)**: Advanced deep learning for time series
- **Occurrence Classification**: Binary classification for payment occurrence prediction
- **Regression Analysis**: Amount prediction with uncertainty quantification

### Interactive Financial Chatbot
- **Natural Language Interface**: Conversational AI for financial queries
- **Multi-Tool Integration**: Access to all financial data through chat
- **Query Capabilities**:
  - Total spending/income for date ranges
  - Last transaction details
  - Monthly financial summaries
  - Bank rates and information
  - Next month predictions
  - Transaction history queries
- **Context Awareness**: Maintains conversation context and user history
- **Smart Classification**: Distinguishes between financial queries and todo tasks
- **Data Sanitization**: Automatic redaction of sensitive information

### Smart Notifications System
- **Real-Time Alerts**: WebSocket-based instant notifications
- **Insufficient Balance Warnings**: Proactive low balance alerts
- **Todo Reminders**: Automated reminders for scheduled tasks
- **Push Notifications**: Mobile app integration with Expo tokens
- **Notification Management**: Mark as read, unread count tracking
- **Account-Specific Alerts**: Targeted notifications for specific accounts
- **Customizable Settings**: User-controlled notification preferences

### Todo & Reminder System
- **Task Creation**: Add financial tasks with dates, times, and amounts
- **Recurring Tasks**: Set up repeating reminders and tasks
- **Task Management**: View, edit, and delete tasks
- **Status Tracking**: Mark tasks as completed or ongoing
- **Smart Reminders**: AI-powered reminder suggestions
- **Integration with Chatbot**: Create todos through natural language
- **Task Details**: Comprehensive task information with descriptions

### Settings & Preferences
- **Notification Controls**: Toggle notification preferences
- **Profile Editing**: Update personal information and contact details
- **Phone Number Management**: Change phone numbers with OTP verification
- **Security Settings**: Manage authentication and security preferences
- **Privacy Controls**: Control data sharing and privacy settings
- **Account Preferences**: Customize account display and behavior

### Technical Features
- **RESTful API**: Comprehensive API endpoints for all features
- **WebSocket Support**: Real-time communication for notifications
- **Database Integration**: MongoDB for scalable data storage
- **Authentication Middleware**: Secure token-based access control
- **CORS Support**: Cross-origin resource sharing for web applications
- **Health Monitoring**: System health checks and status endpoints
- **Error Handling**: Comprehensive error management and logging

### Security Features
- **Data Encryption**: Secure storage and transmission of sensitive data
- **OTP Verification**: Multi-factor authentication for critical operations
- **Token Management**: Secure JWT token handling with refresh capabilities
- **Input Validation**: Comprehensive data validation and sanitization
- **Access Control**: Role-based access to different features
- **Audit Logging**: Track user actions and system events

## Technology Stack

SpendLess is built using modern, scalable technologies that provide robust performance, security, and AI capabilities.

### Backend Framework
- **FastAPI 0.115.11**: High-performance Python web framework with automatic API documentation
- **Uvicorn**: ASGI server for running FastAPI applications
- **Gunicorn**: Production WSGI server for deployment
- **Starlette**: Lightweight ASGI framework (FastAPI dependency)
- **Pydantic 2.11.3**: Data validation and settings management using Python type annotations

### Database & Data Storage
- **MongoDB**: NoSQL database for flexible document storage
- **Motor 3.7.0**: Async MongoDB driver for Python
- **PyMongo 4.11.2**: MongoDB Python driver
- **ChromaDB**: Vector database for AI embeddings and similarity search
- **SQLAlchemy 2.0.38**: SQL toolkit and ORM (for potential relational data needs)

### AI & Machine Learning
- **PyTorch 2.7.1**: Deep learning framework for neural networks
- **NeuralForecast**: Time series forecasting library with N-BEATS implementation
- **N-BEATSx**: Neural basis expansion analysis for time series forecasting
- **Scikit-learn 1.7.0**: Machine learning library for traditional ML algorithms
- **NumPy 2.2.5**: Numerical computing library
- **Pandas 2.3.0**: Data manipulation and analysis
- **SciPy 1.16.0**: Scientific computing library
- **Optuna**: Hyperparameter optimization framework
- **Transformers 4.53.1**: Hugging Face transformers library
- **Sentence-Transformers 5.0.0**: Semantic embeddings for text similarity

### Natural Language Processing
- **spaCy 3.8.4**: Advanced NLP library with pre-trained models
- **en_core_web_sm**: English language model for spaCy
- **NLTK 3.9.1**: Natural Language Toolkit
- **LangChain 0.3.24**: Framework for developing LLM applications
- **LangChain Community 0.3.18**: Community integrations for LangChain
- **LangChain Google GenAI 2.0.11**: Google Gemini integration
- **LangGraph 0.3.2**: Graph-based workflow for LLM applications

### Large Language Models & AI Services
- **Google Generative AI**: Gemini 1.5 Flash and 2.5 Flash models
- **Ollama 0.4.7**: Local LLM deployment and management
- **Hugging Face Hub 0.33.2**: Access to pre-trained models
- **Google AI Generative Language 0.6.16**: Google's generative AI API

### Authentication & Security
- **PyJWT 2.10.1**: JSON Web Token implementation
- **bcrypt 4.3.0**: Password hashing library
- **Argon2-cffi 23.1.0**: Modern password hashing
- **Cryptography 44.0.2**: Cryptographic recipes and primitives
- **Twilio 9.4.6**: SMS and OTP services

### Real-time Communication
- **WebSockets 15.0.1**: Real-time bidirectional communication
- **FastAPI WebSocket**: Built-in WebSocket support
- **AsyncIO**: Asynchronous programming support

### Data Processing & Utilities
- **Python-dotenv 1.0.1**: Environment variable management
- **Pillow 11.3.0**: Python Imaging Library for image processing
- **OpenPyXL 3.1.5**: Excel file reading and writing
- **PyYAML 6.0.2**: YAML parser and emitter
- **Requests 2.32.3**: HTTP library for API calls
- **httpx 0.28.1**: Modern HTTP client with async support

### Development & Deployment
- **Python 3.x**: Programming language
- **Docker**: Containerization (implied for deployment)
- **Environment Variables**: Configuration management
- **CORS Middleware**: Cross-origin resource sharing
- **Health Check Endpoints**: System monitoring

### External APIs & Services
- **Google APIs**: Gemini AI, Google Auth
- **Twilio API**: SMS and communication services
- **Bank APIs**: Integration with banking systems (implied)
- **Expo Push Notifications**: Mobile push notification service

### Data Validation & Serialization
- **Pydantic Settings 2.8.1**: Settings management
- **Marshmallow 3.26.1**: Object serialization/deserialization
- **Dataclasses JSON 0.6.7**: JSON serialization for dataclasses
- **Orjson 3.10.15**: Fast JSON library

### Monitoring & Logging
- **Rich 13.9.4**: Rich text and beautiful formatting
- **Tqdm 4.67.1**: Progress bars for loops
- **Watchfiles 1.1.0**: File system event monitoring

### Development Tools
- **Typer 0.15.2**: CLI framework
- **Click 8.1.8**: Command line interface creation
- **Colorama 0.4.6**: Cross-platform colored terminal text

### Performance & Optimization
- **AsyncIO**: Asynchronous programming
- **Motor**: Async MongoDB driver
- **Aiohttp 3.11.13**: Async HTTP client/server
- **Cachetools 5.5.2**: Caching utilities
- **Tenacity 9.0.0**: Retry library for robust operations

## Project Structure

SpendLess follows a clean, modular architecture with clear separation of concerns. The project is organized into logical directories that separate different aspects of the application.

```
bankingApp/
├── backend/                          # Main backend application
│   ├── AI_services/                  # AI/ML prediction models and services
│   ├── chroma_db/                    # Vector database for AI embeddings
│   ├── routes/                       # API route handlers
│   ├── schemas/                      # Pydantic data models and validation
│   ├── services/                     # Business logic and service layer
│   ├── utils/                        # Utility functions and helpers
│   ├── database.py                   # Database connection and configuration
│   ├── main.py                       # FastAPI application entry point
│   ├── models.py                     # Database models and schemas
│   ├── requirements.txt              # Python dependencies
│   └── README.md                     # Backend documentation
├── documents/                        # Project documentation
│   └── Final_Report_Group_6.pdf     # Project report
└── README.md                         # Main project documentation
```

### Backend Directory Structure

#### `/backend/AI_services/`
Contains all AI and machine learning models and prediction services:

- **`n_beats_total_balance.ipynb`**: N-BEATS model for account balance predictions
- **`amount_regression_total_expence.ipynb`**: Regression model for expense amount prediction
- **`occurence_binary_classification_total_expence.ipynb`**: Binary classification for payment occurrence
- **`category_wise_expense_prediction_tft.ipynb`**: TFT model for category-wise expense predictions
- **`category_wise_expense_income_prdection_nbeats.ipynb`**: N-BEATS for income/expense predictions
- **`add_expense_predictions_to_db.py`**: Service to store expense predictions in database
- **`add_income_predictions_to_db.py`**: Service to store income predictions in database
- **`balancePredict_to_db.py`**: Service to store balance predictions in database
- **`preprocess_*.py`**: Data preprocessing scripts for different models

#### `/backend/routes/`
API route handlers following RESTful principles:

- **`bankAccountManagement.py`**: Bank account CRUD operations
- **`user_login.py`**: User authentication and login endpoints
- **`sign_in.py`**: User registration and sign-up process
- **`dashboard.py`**: Dashboard data and analytics endpoints
- **`transaction_history.py`**: Transaction history and filtering
- **`transaction_categorization.py`**: AI-powered transaction categorization
- **`incomeExpensePredictions.py`**: AI prediction endpoints
- **`chatbot.py`**: Conversational AI chatbot endpoints
- **`notification.py`**: Real-time notification system
- **`todo.py`**: Todo and reminder management
- **`settings.py`**: User settings and preferences
- **`change_password.py`**: Password management
- **`forgot_password.py`**: Password recovery

#### `/backend/schemas/`
Pydantic models for data validation and serialization:

- **`user_login_schemas.py`**: User authentication schemas
- **`bankAccountManagement.py`**: Bank account data models
- **`dashboard.py`**: Dashboard response schemas
- **`transaction_history.py`**: Transaction data models
- **`transaction_categorization.py`**: Categorization schemas
- **`incomeExpenseprediction.py`**: Prediction response models
- **`chatbot.py`**: Chatbot request/response schemas
- **`notification.py`**: Notification data models
- **`todo.py`**: Todo task schemas
- **`settings.py`**: User settings schemas

#### `/backend/services/`
Business logic and service layer implementation:

- **`bankAccountManagement.py`**: Bank account business logic
- **`user_login.py`**: Authentication service logic
- **`sign_in.py`**: Registration service logic
- **`dashboard.py`**: Dashboard data processing
- **`transaction_history.py`**: Transaction data processing
- **`transaction_categorization.py`**: AI categorization logic
- **`incomeExpensePrediction.py`**: Prediction service logic
- **`chatbot.py`**: Chatbot conversation handling
- **`chatbotTest.py`**: Chatbot testing and development
- **`llmAgentTools.py`**: LLM agent tools and functions
- **`clustering.py`**: ML clustering algorithms
- **`notification.py`**: Notification service logic
- **`notification_watcher.py`**: Background notification monitoring
- **`websocket_manager.py`**: WebSocket connection management
- **`todo.py`**: Todo management logic
- **`settings.py`**: Settings management logic

#### `/backend/utils/`
Utility functions and helper modules:

- **`auth.py`**: JWT authentication utilities
- **`encrypt_and_decrypt.py`**: Data encryption/decryption
- **`encrypt_key_generation.py`**: Encryption key generation
- **`imagetobase64.py`**: Image processing utilities
- **`json_utils.py`**: JSON handling utilities
- **`OTP.py`**: OTP generation and validation

#### `/backend/chroma_db/`
Vector database for AI embeddings and similarity search:

- **`chroma.sqlite3`**: ChromaDB SQLite database
- **`7282ffd6-ad0a-47c9-8b74-a3593e8645a9/`**: Vector collection data

### Key Files

#### **`main.py`**
- FastAPI application entry point
- Router registration and middleware setup
- CORS configuration
- WebSocket initialization
- Health check endpoints

#### **`database.py`**
- MongoDB connection configuration
- Database and collection definitions
- Async database client setup
- Environment variable management

#### **`models.py`**
- Pydantic data models for all entities
- Database schema definitions
- Data validation models
- Enum definitions for constants

#### **`requirements.txt`**
- Complete list of Python dependencies
- Version-pinned packages for reproducibility
- AI/ML, web framework, and utility libraries

### Architecture Overview

The application follows a **layered architecture** pattern:

1. **Presentation Layer** (`routes/`): API endpoints and request handling
2. **Business Logic Layer** (`services/`): Core business logic and data processing
3. **Data Access Layer** (`database.py`, `models.py`): Database operations and data models
4. **AI/ML Layer** (`AI_services/`): Machine learning models and predictions
5. **Utility Layer** (`utils/`): Shared utilities and helper functions

### Design Patterns

- **Repository Pattern**: Database operations abstracted through services
- **Dependency Injection**: FastAPI's built-in DI for route dependencies
- **Async/Await**: Asynchronous programming throughout the application
- **Modular Design**: Clear separation of concerns with dedicated directories
- **Schema Validation**: Pydantic models for request/response validation
- **Middleware Pattern**: Authentication and CORS middleware
- **Observer Pattern**: WebSocket-based real-time notifications

### Data Flow

1. **Request** → Routes (validation) → Services (business logic) → Database
2. **AI Predictions** → AI Services → Database → API Response
3. **Real-time Updates** → WebSocket Manager → Client Notifications
4. **Authentication** → JWT Middleware → Route Access Control

## Installation & Setup

This guide will help you set up the SpendLess banking application on your local development environment.

### Prerequisites

Before starting the installation, ensure you have the following installed on your system:

- **Python 3.8+**: Required for running the FastAPI application
- **MongoDB**: Database server (local installation or MongoDB Atlas)
- **Git**: For cloning the repository
- **Virtual Environment**: Python virtual environment (recommended)

### Environment Setup

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd spendless/bankingApp/backend
   ```

2. **Create Virtual Environment**
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Create Environment Variables File**
   
   Create a `.env` file in the `backend` directory with the following variables:

   ```env
   # Database Configuration
   MONGO_URI=mongodb://localhost:27017/spendless
   # For MongoDB Atlas: mongodb+srv://username:password@cluster.mongodb.net/spendless

   # JWT Authentication
   SECRET_KEY=your-super-secret-jwt-key-here
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   REFRESH_TOKEN_EXPIRE_MINUTES=10080

   # Google Gemini AI API
   GEMINI_API_KEY=your-google-gemini-api-key

   # SMS Service (Notify.lk)
   NOTIFY_LK_USER_ID=your-notify-lk-user-id
   NOTIFY_LK_API_KEY=your-notify-lk-api-key
   NOTIFY_LK_SENDER_ID=your-approved-sender-id

   # Optional: Twilio Configuration (if using Twilio instead of Notify.lk)
   TWILIO_ACCOUNT_SID=your-twilio-account-sid
   TWILIO_AUTH_TOKEN=your-twilio-auth-token
   TWILIO_PHONE_NUMBER=your-twilio-phone-number
   ```

   **Important**: Add `.env` to your `.gitignore` file to prevent committing sensitive information [[memory:7097700]].

### Dependencies Installation

1. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install spaCy Language Model**
   ```bash
   python -m spacy download en_core_web_sm
   ```

3. **Install NLTK Data**
   ```bash
   python -c "import nltk; nltk.download('words')"
   ```

### Database Setup

1. **MongoDB Installation**

   **Option A: Local MongoDB Installation**
   ```bash
   # On Ubuntu/Debian:
   sudo apt-get install mongodb

   # On macOS with Homebrew:
   brew install mongodb-community

   # On Windows:
   # Download and install from https://www.mongodb.com/try/download/community
   ```

   **Option B: MongoDB Atlas (Cloud)**
   - Create account at [MongoDB Atlas](https://www.mongodb.com/atlas)
   - Create a new cluster
   - Get connection string and update `MONGO_URI` in `.env`

2. **Start MongoDB Service**
   ```bash
   # On Ubuntu/Debian:
   sudo systemctl start mongod

   # On macOS:
   brew services start mongodb-community

   # On Windows:
   # MongoDB should start automatically after installation
   ```

3. **Verify Database Connection**
   ```bash
   # Test MongoDB connection
   mongosh
   # or
   mongo
   ```

### API Keys Setup

1. **Google Gemini API Key**
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Add to `.env` file as `GEMINI_API_KEY`

2. **SMS Service Setup**
   
   **Option A: Notify.lk (Sri Lanka)**
   - Register at [Notify.lk](https://notify.lk)
   - Get your User ID, API Key, and Sender ID
   - Add to `.env` file

   **Option B: Twilio (International)**
   - Sign up at [Twilio](https://www.twilio.com)
   - Get Account SID, Auth Token, and Phone Number
   - Add to `.env` file

### Initial Configuration

1. **Generate Encryption Key**
   ```bash
   cd utils
   python encrypt_key_generation.py
   ```

2. **Initialize ChromaDB**
   ```bash
   # ChromaDB will be initialized automatically on first run
   # Ensure the chroma_db directory has proper permissions
   ```

3. **Create Required Directories**
   ```bash
   mkdir -p chroma_db
   mkdir -p logs
   ```

### Running the Application

1. **Start the Development Server**
   ```bash
   # Using Uvicorn directly
   uvicorn main:app --reload --host 0.0.0.0 --port 8000

   # Or using Python
   python -m uvicorn main:app --reload
   ```

2. **Verify Installation**
   - Open browser and navigate to `http://localhost:8000`
   - Check health endpoint: `http://localhost:8000/health`
   - View API documentation: `http://localhost:8000/docs`

### Production Setup

1. **Install Production Dependencies**
   ```bash
   pip install gunicorn
   ```

2. **Run with Gunicorn**
   ```bash
   gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
   ```

3. **Environment Variables for Production**
   - Use secure, randomly generated `SECRET_KEY`
   - Set up proper MongoDB authentication
   - Configure CORS origins appropriately
   - Use environment-specific API keys

### Docker Setup (Optional)

1. **Create Dockerfile**
   ```dockerfile
   FROM python:3.9-slim

   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt

   COPY . .
   EXPOSE 8000

   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

2. **Create docker-compose.yml**
   ```yaml
   version: '3.8'
   services:
     app:
       build: .
       ports:
         - "8000:8000"
       environment:
         - MONGO_URI=mongodb://mongo:27017/spendless
       depends_on:
         - mongo
     
     mongo:
       image: mongo:latest
       ports:
         - "27017:27017"
   ```

3. **Run with Docker**
   ```bash
   docker-compose up --build
   ```

### Troubleshooting

**Common Issues:**

1. **MongoDB Connection Error**
   - Verify MongoDB is running
   - Check connection string in `.env`
   - Ensure network connectivity

2. **spaCy Model Not Found**
   ```bash
   python -m spacy download en_core_web_sm
   ```

3. **Import Errors**
   - Ensure virtual environment is activated
   - Verify all dependencies are installed
   - Check Python path

4. **API Key Issues**
   - Verify API keys are correctly set in `.env`
   - Check API key permissions and quotas
   - Ensure no extra spaces in environment variables

5. **Port Already in Use**
   ```bash
   # Find process using port 8000
   lsof -i :8000
   # Kill the process or use different port
   uvicorn main:app --port 8001
   ```

### Next Steps

After successful installation:

1. **Test API Endpoints**: Use the interactive docs at `/docs`
2. **Set Up Frontend**: Configure your frontend application to connect to the API
3. **Configure AI Models**: Train and deploy your prediction models
4. **Set Up Monitoring**: Implement logging and monitoring for production use

### Development Tips

- Use `--reload` flag with uvicorn for automatic reloading during development
- Check logs in the terminal for debugging information
- Use FastAPI's automatic documentation at `/docs` and `/redoc`
- Test WebSocket connections using tools like Postman or custom clients

## Configuration

This section covers all configuration options, environment variables, and settings for the SpendLess banking application.

### Environment Variables

The application uses environment variables for configuration. Create a `.env` file in the `backend` directory with the following variables:

#### Database Configuration
```env
# MongoDB Connection
MONGO_URI=mongodb://localhost:27017/spendless
# For MongoDB Atlas: mongodb+srv://username:password@cluster.mongodb.net/spendless
```

#### JWT Authentication Configuration
```env
# JWT Secret Key (Generate a secure random string)
SECRET_KEY=your-super-secret-jwt-key-here

# JWT Algorithm
ALGORITHM=HS256

# Token Expiration Times (in minutes)
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_MINUTES=10080
```

#### AI/ML Service Configuration
```env
# Google Gemini AI API
GEMINI_API_KEY=your-google-gemini-api-key

# Optional: Ollama Configuration (for local LLM)
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama2
```

#### SMS Service Configuration
```env
# Notify.lk (Sri Lanka SMS Service)
NOTIFY_LK_USER_ID=your-notify-lk-user-id
NOTIFY_LK_API_KEY=your-notify-lk-api-key
NOTIFY_LK_SENDER_ID=your-approved-sender-id

# Twilio (International SMS Service) - Alternative
TWILIO_ACCOUNT_SID=your-twilio-account-sid
TWILIO_AUTH_TOKEN=your-twilio-auth-token
TWILIO_PHONE_NUMBER=your-twilio-phone-number
```

#### Push Notification Configuration
```env
# Expo Push Notifications
EXPO_ACCESS_TOKEN=your-expo-access-token
```

#### Application Configuration
```env
# Application Settings
APP_NAME=SpendLess
APP_VERSION=1.0.0
DEBUG=True
LOG_LEVEL=INFO

# Server Configuration
HOST=0.0.0.0
PORT=8000
WORKERS=4

# CORS Configuration
CORS_ORIGINS=http://localhost:3000,http://localhost:8080
CORS_CREDENTIALS=True
CORS_METHODS=GET,POST,PUT,DELETE,OPTIONS
CORS_HEADERS=*
```

### Database Configuration

#### MongoDB Collections
The application uses the following MongoDB collections:

- **`user`**: User accounts and profiles
- **`account`**: Bank account information
- **`bank`**: Bank details and rates
- **`transaction`**: Transaction history
- **`transaction_category`**: Transaction categories
- **`predicted_balance`**: AI balance predictions
- **`predicted_expense`**: AI expense predictions
- **`predicted_income`**: AI income predictions
- **`notification`**: User notifications
- **`Todo-list`**: Todo and reminder tasks
- **`chatbot`**: Chatbot conversation history
- **`chatbot_details`**: Chatbot configuration
- **`OTP`**: OTP verification codes
- **`goal`**: Financial goals
- **`credit_periods`**: Credit card billing periods
- **`user_dummy`**: Dummy data for testing
- **`category_name_changes`**: Category modification history
- **`transaction_category_changes`**: Transaction categorization changes
- **`expo_tokens`**: Push notification tokens

#### Database Indexes
For optimal performance, create the following indexes:

```javascript
// User collection indexes
db.user.createIndex({ "user_id": 1 }, { unique: true })
db.user.createIndex({ "login_nic": 1 }, { unique: true })
db.user.createIndex({ "phone_number": 1 })

// Account collection indexes
db.account.createIndex({ "user_id": 1 })
db.account.createIndex({ "account_id": 1 }, { unique: true })
db.account.createIndex({ "account_number": 1 })

// Transaction collection indexes
db.transaction.createIndex({ "account_id": 1 })
db.transaction.createIndex({ "date": -1 })
db.transaction.createIndex({ "user_id": 1, "date": -1 })

// Notification collection indexes
db.notification.createIndex({ "user_id": 1, "created_at": -1 })
db.notification.createIndex({ "user_id": 1, "seen": 1 })
```

### AI Model Configuration

#### Chatbot Configuration
```python
# Chatbot model settings
CHATBOT_MODEL = "gemini-1.5-flash"  # or "gemini-2.5-flash"
CHATBOT_TEMPERATURE = 0.7
CHATBOT_MAX_TOKENS = 1000
CHATBOT_MEMORY_SIZE = 10  # Number of previous messages to remember
```

#### Prediction Model Configuration
```python
# N-BEATS Model Configuration
NBEATS_INPUT_SIZE = 14  # Historical data points
NBEATS_HORIZON = 30     # Prediction horizon (days)
NBEATS_DROPOUT = 0.1    # Dropout probability
NBEATS_MAX_STEPS = 200  # Training steps

# TFT Model Configuration
TFT_INPUT_SIZE = 21     # Historical data points
TFT_HORIZON = 30        # Prediction horizon (days)
TFT_HIDDEN_SIZE = 64    # Hidden layer size
TFT_ATTENTION_HEAD_SIZE = 4  # Attention heads
```

### Security Configuration

#### Encryption Settings
```env
# Data Encryption
ENCRYPTION_KEY=your-32-character-encryption-key
ENCRYPTION_ALGORITHM=AES-256-GCM
```

#### Rate Limiting
```python
# API Rate Limiting
RATE_LIMIT_REQUESTS = 100  # Requests per minute
RATE_LIMIT_WINDOW = 60     # Time window in seconds
RATE_LIMIT_BURST = 10      # Burst allowance
```

#### CORS Configuration
```python
# CORS Settings for Production
CORS_ORIGINS = [
    "https://yourdomain.com",
    "https://app.yourdomain.com",
    "https://admin.yourdomain.com"
]

# Development CORS (permissive)
CORS_ORIGINS_DEV = ["*"]
```

### Notification Configuration

#### WebSocket Settings
```python
# WebSocket Configuration
WEBSOCKET_HEARTBEAT_INTERVAL = 30  # seconds
WEBSOCKET_MAX_CONNECTIONS = 1000
WEBSOCKET_MESSAGE_SIZE_LIMIT = 1024  # bytes
```

#### Push Notification Settings
```python
# Push Notification Configuration
PUSH_NOTIFICATION_BATCH_SIZE = 100
PUSH_NOTIFICATION_RETRY_ATTEMPTS = 3
PUSH_NOTIFICATION_TIMEOUT = 30  # seconds
```

### Logging Configuration

#### Log Levels
```env
# Logging Configuration
LOG_LEVEL=INFO  # DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FORMAT=%(asctime)s - %(name)s - %(levelname)s - %(message)s
LOG_FILE=logs/spendless.log
LOG_MAX_SIZE=10MB
LOG_BACKUP_COUNT=5
```

#### Log Categories
- **Authentication**: Login attempts, token generation
- **API**: Request/response logging
- **Database**: Query performance and errors
- **AI/ML**: Model predictions and errors
- **Notifications**: SMS and push notification delivery
- **Security**: Failed authentication attempts, suspicious activity

### Performance Configuration

#### Caching Settings
```python
# Redis Cache Configuration (if using Redis)
REDIS_URL=redis://localhost:6379/0
CACHE_TTL=3600  # seconds
CACHE_MAX_SIZE=1000  # items
```

#### Database Connection Pool
```python
# MongoDB Connection Pool
MONGO_MAX_POOL_SIZE=100
MONGO_MIN_POOL_SIZE=10
MONGO_MAX_IDLE_TIME=30000  # milliseconds
MONGO_CONNECT_TIMEOUT=20000  # milliseconds
```

### Development Configuration

#### Debug Settings
```env
# Development Settings
DEBUG=True
RELOAD=True
LOG_LEVEL=DEBUG
ENABLE_SWAGGER=True
ENABLE_REDOC=True
```

#### Testing Configuration
```env
# Testing Settings
TEST_DATABASE_URL=mongodb://localhost:27017/spendless_test
TEST_MODE=True
MOCK_EXTERNAL_APIS=True
```

### Production Configuration

#### Security Headers
```python
# Security Headers
SECURITY_HEADERS = {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "X-XSS-Protection": "1; mode=block",
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
    "Content-Security-Policy": "default-src 'self'"
}
```

#### Monitoring Configuration
```env
# Monitoring and Metrics
ENABLE_METRICS=True
METRICS_PORT=9090
HEALTH_CHECK_INTERVAL=30  # seconds
```

### Configuration Validation

#### Environment Variable Validation
The application validates required environment variables on startup:

```python
# Required variables
REQUIRED_VARS = [
    "MONGO_URI",
    "SECRET_KEY",
    "GEMINI_API_KEY"
]

# Optional variables with defaults
OPTIONAL_VARS = {
    "ACCESS_TOKEN_EXPIRE_MINUTES": 30,
    "REFRESH_TOKEN_EXPIRE_MINUTES": 10080,
    "LOG_LEVEL": "INFO",
    "DEBUG": False
}
```

### Configuration Management

#### Environment-Specific Configs
- **Development**: `.env.development`
- **Staging**: `.env.staging`
- **Production**: `.env.production`

#### Configuration Loading Order
1. Default values (hardcoded)
2. Environment variables
3. `.env` file
4. Command line arguments

### Best Practices

1. **Never commit `.env` files** to version control
2. **Use strong, unique secrets** for production
3. **Rotate API keys regularly**
4. **Monitor configuration changes**
5. **Use environment-specific configurations**
6. **Validate all configuration on startup**
7. **Document all configuration options**
8. **Use configuration management tools** for production

### Configuration Examples

#### Minimal Development Setup
```env
MONGO_URI=mongodb://localhost:27017/spendless
SECRET_KEY=dev-secret-key-change-in-production
GEMINI_API_KEY=your-gemini-api-key
DEBUG=True
```

#### Production Setup
```env
MONGO_URI=mongodb+srv://user:pass@cluster.mongodb.net/spendless
SECRET_KEY=super-secure-random-key-32-chars-min
GEMINI_API_KEY=your-production-gemini-key
NOTIFY_LK_USER_ID=your-production-user-id
NOTIFY_LK_API_KEY=your-production-api-key
NOTIFY_LK_SENDER_ID=your-approved-sender
DEBUG=False
LOG_LEVEL=WARNING
```

## API Documentation
- Authentication endpoints
- User management
- Bank account operations
- Transaction management
- AI prediction endpoints
- Notification system
- Chatbot integration

## AI/ML Services
- Balance prediction models
- Expense/Income forecasting
- Transaction categorization
- N-BEATS implementation
- TFT (Temporal Fusion Transformer)
- Model training and deployment

## Database Schema
- User models
- Account models
- Transaction models
- Prediction models
- Notification models

## Usage Examples
- Basic API calls
- Authentication flow
- Transaction operations
- AI prediction usage
- Chatbot interactions

## Development
- Local development setup
- Code structure guidelines
- Adding new features
- Debugging tips

## Testing
- Unit testing
- Integration testing
- API testing
- Model validation

## Deployment
- Production setup
- Environment configuration
- Scaling considerations
- Monitoring

## Contributing
- Development workflow
- Code standards
- Pull request process
- Issue reporting

## License
- License information

## Contact
- Team information
- Support channels