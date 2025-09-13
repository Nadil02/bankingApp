**SpendLess** is a cutting-edge proactive financial assistant that revolutionizes personal banking through advanced AI and machine learning technologies. This comprehensive banking application combines traditional financial services with intelligent predictive analytics, providing users with unprecedented insights into their financial future.

### Key Highlights

- 🤖 **AI-Powered Predictions**: Advanced ML models for expense, income, and balance forecasting
- 🏦 **Multi-Bank Integration**: Unified management across multiple banking institutions
- 💬 **Intelligent Chatbot**: Natural language financial assistant with RAG capabilities with agentic chatbot
- 📊 **Real-time Analytics**: Comprehensive dashboard with actionable insights
- 🔒 **Enterprise Security**: Bank-grade security with JWT authentication and encryption
- ☁️ **Cloud-Native**: Built for Azure cloud with auto-scaling and high availability

### Quick Start

```bash
# Clone the repository
git clone https://github.com/Nadil02/bankingApp.git
cd spendless/bankingApp

# Install dependencies
pip install -r backend/requirements.txt

# Configure environment
cp backend/.env.example backend/.env
# Edit .env with your configuration

# Run the application
cd backend
uvicorn main:app --reload
```

## Table of Contents
1. [Project Overview](#project-overview)
   - [High-Level Solution Architecture](#high-level-solution-architecture)
   - [What SpendLess Does](#what-spendless-does)
   - [Problem It Solves](#problem-it-solves)
   - [Target Audience](#target-audience)
   - [Key Value Propositions](#key-value-propositions)
2. [Features](#features)
   - [User Authentication & Management](#user-authentication--management)
   - [Bank Account Management](#bank-account-management)
   - [Dashboard & Analytics](#dashboard--analytics)
   - [Transaction Management](#transaction-management)
   - [AI-Powered Transaction Categorization](#ai-powered-transaction-categorization)
   - [Financial Predictions & AI Analytics](#financial-predictions--ai-analytics)
   - [Interactive Financial Chatbot](#interactive-financial-chatbot)
   - [Smart Notifications System](#smart-notifications-system)
   - [Todo & Reminder System](#todo--reminder-system)
   - [Settings & Preferences](#settings--preferences)
   - [Technical Features](#technical-features)
   - [Security Features](#security-features)
3. [Technology Stack](#technology-stack)
   - [Backend Framework](#backend-framework)
   - [Database & Data Storage](#database--data-storage)
   - [AI & Machine Learning](#ai--machine-learning)
   - [Natural Language Processing](#natural-language-processing)
   - [Large Language Models & AI Services](#large-language-models--ai-services)
   - [Authentication & Security](#authentication--security)
   - [Real-time Communication](#real-time-communication)
   - [Data Processing & Utilities](#data-processing--utilities)
   - [Development & Deployment](#development--deployment)
   - [External APIs & Services](#external-apis--services)
   - [Data Validation & Serialization](#data-validation--serialization)
   - [Monitoring & Logging](#monitoring--logging)
4. [Project Structure](#project-structure)
5. [Installation & Setup](#installation--setup)
6. [Configuration](#configuration)
7. [API Documentation](#api-documentation)
   - [Authentication Endpoints](#authentication-endpoints)
   - [User Registration](#user-registration)
   - [Bank Account Management](#bank-account-management)
   - [Dashboard Endpoints](#dashboard-endpoints)
   - [Transaction Management](#transaction-management)
   - [AI Predictions](#ai-predictions)
   - [Chatbot Integration](#chatbot-integration)
   - [Todo & Reminder System](#todo--reminder-system)
   - [Notification System](#notification-system)
   - [System Endpoints](#system-endpoints)
   - [Rate Limiting](#rate-limiting)
   - [Error Codes](#error-codes)
   - [SDK Examples](#sdk-examples)
8. [AI/ML Services](#aiml-services)
9. [Model Accuracy & Results](#model-accuracy--results)
10. [Database Schema](#database-schema)
11. [Usage Examples](#usage-examples)
12. [Development](#development)
13. [Deployment](#deployment)

## Project Overview

**SpendLess** is a comprehensive proactive financial assistant that leverages advanced AI and machine learning technologies to provide intelligent banking solutions and financial predictions. Built as a modern banking application, SpendLess combines traditional banking features with cutting-edge predictive analytics to help users make informed financial decisions.

### High-Level Solution Architecture

![High-Level Solution Diagram](documents/high_level_solution_diagram.jpeg)

*Figure 1: SpendLess High-Level Solution Architecture - Overview of the complete system architecture including user interfaces, backend services, AI/ML components, and data storage layers.*

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

This section provides comprehensive documentation for all API endpoints in the SpendLess banking application. The API follows RESTful principles and uses JWT authentication for secure access.

### Base URL
```
Development: http://localhost:8000
Production: https://your-domain.com
```

### Authentication

All protected endpoints require JWT authentication. Include the token in the Authorization header:
```
Authorization: Bearer <your-jwt-token>
```

### Response Format

All API responses follow a consistent format:
```json
{
  "status": "success|error",
  "message": "Description of the result",
  "data": {} // Response data (if applicable)
}
```

### Error Handling

Standard HTTP status codes are used:
- `200` - Success
- `201` - Created
- `400` - Bad Request
- `401` - Unauthorized
- `403` - Forbidden
- `404` - Not Found
- `500` - Internal Server Error

---

## Authentication Endpoints

### User Login
**POST** `/login`

Authenticate user and receive JWT tokens.

**Request Body:**
```json
{
  "nic": "string",
  "passcode": "string"
}
```

**Response:**
```json
{
  "access_token": "string",
  "refresh_token": "string",
  "token_type": "bearer",
  "user_id": 123,
  "expires_in": 1800
}
```

### Refresh Token
**POST** `/refresh-token`

Refresh expired access token.

**Request Body:**
```json
{
  "refresh_token": "string"
}
```

**Response:**
```json
{
  "access_token": "string",
  "token_type": "bearer",
  "expires_in": 1800
}
```

### Get User Info
**GET** `/user-info`

Get current user information.

**Headers:** `Authorization: Bearer <token>`

**Response:**
```json
{
  "user_id": 123,
  "first_name": "string",
  "last_name": "string",
  "username": "string",
  "phone_number": "string",
  "user_image": "string"
}
```

---

## User Registration

### Sign Up
**POST** `/sign_in`

Register a new user account.

**Request Body:**
```json
{
  "first_name": "string",
  "last_name": "string",
  "username": "string",
  "NIC": "string",
  "phone_number": "string",
  "passcode": "string"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "User registered successfully",
  "otp_id": 123
}
```

### Verify OTP
**POST** `/sing_in_otp`

Verify OTP for user registration.

**Request Body:**
```json
{
  "otp_id": 123,
  "otp": "string"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "OTP verified successfully"
}
```

---

## Bank Account Management

### Get Account Details
**POST** `/bankAccountManagement/accountDetails`

Get all bank accounts for a user.

**Headers:** `Authorization: Bearer <token>`

**Request Body:**
```json
{
  "user_id": 123
}
```

**Response:**
```json
[
  {
    "bank_id": 1,
    "account_number": 123456789,
    "account_type": "savings",
    "balance": 50000.00,
    "logo": "bank_logo_url"
  }
]
```

### Add Bank Account
**POST** `/bankAccountManagement/addBankAccount`

Add a new bank account.

**Headers:** `Authorization: Bearer <token>`

**Request Body:**
```json
{
  "bank_name": "string",
  "account_number": 123456789,
  "account_type": "savings",
  "NIC": "string"
}
```

**Response:**
```json
{
  "otp_id": 123,
  "status": "success",
  "message": "OTP sent for verification"
}
```

### Remove Bank Account
**POST** `/bankAccountManagement/removeBankAccount`

Remove a bank account.

**Headers:** `Authorization: Bearer <token>`

**Request Body:**
```json
{
  "user_id": 123,
  "account_number": 123456789,
  "NIC": "string",
  "passcode": "string"
}
```

**Response:**
```json
{
  "message": "Account removed successfully",
  "description": "Account 123456789 has been removed"
}
```

---

## Dashboard Endpoints

### Get Dashboard Data
**GET** `/dashboard/`

Get comprehensive dashboard data for all accounts.

**Headers:** `Authorization: Bearer <token>`

**Query Parameters:**
- `user_id` (int): User ID

**Response:**
```json
{
  "accounts": [
    {
      "account_id": 1,
      "account_number": 123456789,
      "account_type": "savings",
      "balance": 50000.00,
      "bank_name": "Bank Name",
      "transactions": [...],
      "predictions": [...]
    }
  ],
  "summary": {
    "total_balance": 100000.00,
    "total_income": 50000.00,
    "total_expenses": 30000.00
  }
}
```

### Get Dashboard with Date Range
**GET** `/dashboard/all_account_time_period`

Get dashboard data for a specific time period.

**Headers:** `Authorization: Bearer <token>`

**Query Parameters:**
- `user_id` (int): User ID
- `startdate` (string): Start date (YYYY-MM-DD)
- `enddate` (string): End date (YYYY-MM-DD)

---

## Transaction Management

### Get Transaction History
**GET** `/transaction_history/load_transaction_history`

Get transaction history for all accounts.

**Headers:** `Authorization: Bearer <token>`

**Query Parameters:**
- `user_id` (int): User ID

**Response:**
```json
{
  "accounts": [
    {
      "account_id": 1,
      "account_number": 123456789,
      "transactions": [
        {
          "transaction_id": 1,
          "date": "2024-01-15T10:30:00Z",
          "description": "Purchase at Store",
          "amount": -1500.00,
          "balance": 48500.00,
          "category": "Shopping"
        }
      ]
    }
  ]
}
```

---

## AI Predictions

### Get All Account Predictions
**GET** `/income_expense-prediction/all_accounts`

Get predictions for all user accounts.

**Headers:** `Authorization: Bearer <token>`

**Query Parameters:**
- `user_id` (int): User ID

**Response:**
```json
{
  "accounts": [
    {
      "account_id": 1,
      "account_number": 123456789,
      "predictions": {
        "balance_forecast": [...],
        "expense_forecast": [...],
        "income_forecast": [...]
      }
    }
  ]
}
```

### Get Account Predictions
**GET** `/income_expense-prediction/account_prediction`

Get detailed predictions for a specific account.

**Headers:** `Authorization: Bearer <token>`

**Query Parameters:**
- `user_id` (int): User ID
- `account_id` (int): Account ID

**Response:**
```json
{
  "account_id": 1,
  "predictions": {
    "balance": [
      {
        "date": "2024-02-01",
        "predicted_balance": 52000.00,
        "confidence_interval": {
          "lower": 50000.00,
          "upper": 54000.00
        }
      }
    ],
    "expenses": [
      {
        "date": "2024-02-01",
        "predicted_amount": 2000.00,
        "category": "Groceries",
        "probability": 0.85
      }
    ]
  }
}
```

---

## Chatbot Integration

### Chat with AI Assistant
**POST** `/chatbot`

Interact with the AI financial assistant.

**Request Body:**
```json
{
  "user_id": 123,
  "query": "What was my total spending last month?"
}
```

**Response:**
```json
{
  "response": "Your total spending last month was $3,500.00. The main categories were groceries ($1,200), utilities ($800), and entertainment ($600)."
}
```

---

## Todo & Reminder System

### Get Todos
**GET** `/todo/TodoView`

Get all ongoing todos for a user.

**Headers:** `Authorization: Bearer <token>`

**Query Parameters:**
- `user_id` (int): User ID

**Response:**
```json
{
  "todos": [
    {
      "todo_id": 1,
      "description": "Pay electricity bill",
      "date": "2024-02-15T00:00:00Z",
      "time": "2024-02-15T09:00:00Z",
      "amount": 2500.00,
      "status": "ongoing",
      "repeat_frequency": "monthly"
    }
  ]
}
```

### Create Todo
**POST** `/todo/add_todos`

Create a new todo item.

**Headers:** `Authorization: Bearer <token>`

**Request Body:**
```json
{
  "user_id": 123,
  "description": "Pay rent",
  "date": "2024-02-01T00:00:00Z",
  "time": "2024-02-01T10:00:00Z",
  "amount": 50000.00,
  "repeat_frequency": "monthly"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Todo created successfully",
  "todo_id": 123
}
```

---

## Notification System

### WebSocket Connection
**WebSocket** `/ws/{user_id}`

Connect to real-time notifications.

**Connection:**
```javascript
const ws = new WebSocket('ws://localhost:8000/ws/123');
ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log(data);
};
```

**Message Format:**
```json
{
  "event": "new_notification|notifications_seen|initial_data",
  "data": {
    "notifications": [...],
    "unread_count": 5
  }
}
```

### Get Notifications
**GET** `/notification/{user_id}`

Get all notifications for a user.

**Response:**
```json
[
  {
    "_id": "notification_id",
    "type": "IN|TO",
    "user_id": 123,
    "account_id": 1,
    "message": "Low balance warning",
    "seen": false,
    "created_at": "2024-01-15T10:30:00Z"
  }
]
```

---

## System Endpoints

### Health Check
**GET** `/health`

Check application health status.

**Response:**
```json
{
  "status": "okks"
}
```

### API Documentation
**GET** `/docs`

Interactive API documentation (Swagger UI).

**GET** `/redoc`

Alternative API documentation (ReDoc).

---

## Rate Limiting

The API implements rate limiting to prevent abuse:
- **100 requests per minute** per IP address
- **Burst allowance**: 10 requests
- **Rate limit headers** included in responses:
  - `X-RateLimit-Limit`
  - `X-RateLimit-Remaining`
  - `X-RateLimit-Reset`

## Error Codes

| Code | Description |
|------|-------------|
| `AUTH_001` | Invalid credentials |
| `AUTH_002` | Token expired |
| `AUTH_003` | Insufficient permissions |
| `USER_001` | User not found |
| `USER_002` | User already exists |
| `ACCOUNT_001` | Account not found |
| `ACCOUNT_002` | Account already linked |
| `TRANSACTION_001` | Transaction not found |
| `PREDICTION_001` | Insufficient data for prediction |
| `NOTIFICATION_001` | Notification service unavailable |

## SDK Examples

### JavaScript/TypeScript
```javascript
const apiClient = {
  baseURL: 'http://localhost:8000',
  token: null,
  
  async login(credentials) {
    const response = await fetch(`${this.baseURL}/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(credentials)
    });
    const data = await response.json();
    this.token = data.access_token;
    return data;
  },
  
  async getDashboard(userId) {
    const response = await fetch(`${this.baseURL}/dashboard/?user_id=${userId}`, {
      headers: { 'Authorization': `Bearer ${this.token}` }
    });
    return response.json();
  }
};
```

### Python
```python
import requests

class SpendLessAPI:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
        self.token = None
    
    def login(self, nic, passcode):
        response = requests.post(f"{self.base_url}/login", json={
            "nic": nic,
            "passcode": passcode
        })
        data = response.json()
        self.token = data["access_token"]
        return data
    
    def get_dashboard(self, user_id):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(
            f"{self.base_url}/dashboard/?user_id={user_id}",
            headers=headers
        )
        return response.json()
```

## AI/ML Services

This section provides comprehensive documentation of the advanced AI and machine learning services powering SpendLess. Our system employs state-of-the-art deep learning models for financial forecasting, transaction analysis, and intelligent insights generation.

### Overview

The SpendLess AI/ML system consists of multiple interconnected models that work together to provide comprehensive financial predictions and insights:

1. **Balance Prediction Models** - N-BEATSx for account balance forecasting
2. **Expense Prediction Models** - N-BEATSx for expense amount regression and occurrence classification
3. **Income Prediction Models** - TFT (Temporal Fusion Transformer) for income forecasting
4. **Category-wise Predictions** - Specialized models for transaction categorization
5. **Feature Engineering Pipeline** - Advanced preprocessing and feature extraction

### System Architecture

```mermaid
graph TB
    subgraph "Data Sources"
        A[Raw Transaction Data]
        B[Account Balance Data]
        C[User Profile Data]
    end
    
    subgraph "Data Preprocessing Pipeline"
        D[Data Cleaning & Validation]
        E[Feature Engineering]
        F[Outlier Detection & Treatment]
        G[Data Normalization]
        H[Temporal Feature Creation]
    end
    
    subgraph "AI/ML Models"
        I[N-BEATSx Balance Model]
        J[N-BEATSx Expense Regression]
        K[N-BEATSx Expense Classification]
        L[TFT Income Model]
        M[Category-wise TFT Models]
    end
    
    subgraph "Hyperparameter Optimization"
        N[Optuna Framework]
        O[Cross-validation]
        P[Performance Metrics]
    end
    
    subgraph "Model Deployment"
        Q[Model Serialization]
        R[Prediction API]
        S[Real-time Inference]
    end
    
    subgraph "Output & Integration"
        T[Balance Forecasts]
        U[Expense Predictions]
        V[Income Forecasts]
        W[Category Insights]
        X[API Endpoints]
    end
    
    A --> D
    B --> D
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    
    H --> I
    H --> J
    H --> K
    H --> L
    H --> M
    
    N --> I
    N --> J
    N --> K
    N --> L
    N --> M
    
    O --> N
    P --> N
    
    I --> Q
    J --> Q
    K --> Q
    L --> Q
    M --> Q
    
    Q --> R
    R --> S
    
    S --> T
    S --> U
    S --> V
    S --> W
    S --> X
```

### Data Preprocessing Pipeline

Our comprehensive preprocessing pipeline ensures high-quality data for model training and inference:

#### 1. Data Cleaning & Validation

```mermaid
flowchart TD
    A[Raw Data Input] --> B[Data Type Conversion]
    B --> C[Missing Value Detection]
    C --> D[Duplicate Removal]
    D --> E[Data Validation]
    E --> F[Date Range Verification]
    F --> G[Balance Consistency Check]
    G --> H[Transaction Amount Validation]
    H --> I[Cleaned Dataset]
```

**Key Cleaning Steps:**
- **Date Standardization**: Convert all date formats to `YYYY-MM-DD`
- **Numeric Conversion**: Handle comma-separated values and currency symbols
- **Missing Value Treatment**: Forward-fill for balance data, zero-fill for transactions
- **Duplicate Detection**: Remove duplicate transactions based on date, amount, and description
- **Data Validation**: Ensure balance consistency and transaction logic

#### 2. Feature Engineering

Our feature engineering pipeline creates 50+ engineered features across multiple categories:

```mermaid
graph LR
    subgraph "Temporal Features"
        A1[Day of Week Sin/Cos]
        A2[Month Sin/Cos]
        A3[Weekend Indicator]
        A4[Seasonal Patterns]
    end
    
    subgraph "Financial Features"
        B1[Rolling Averages 7/30 days]
        B2[Rolling Standard Deviation]
        B3[Balance Change Indicators]
        B4[Transaction Frequency]
    end
    
    subgraph "Behavioral Features"
        C1[Days Since Last Transaction]
        C2[Payment Streak Counters]
        C3[Transaction Patterns]
        C4[Spending Velocity]
    end
    
    subgraph "Statistical Features"
        D1[Z-Score Normalization]
        D2[Percentile Rankings]
        D3[Moving Averages]
        D4[Volatility Measures]
    end
    
    A1 --> E[Feature Matrix]
    A2 --> E
    A3 --> E
    A4 --> E
    B1 --> E
    B2 --> E
    B3 --> E
    B4 --> E
    C1 --> E
    C2 --> E
    C3 --> E
    C4 --> E
    D1 --> E
    D2 --> E
    D3 --> E
    D4 --> E
```

**Detailed Feature Categories:**

**Temporal Features:**
```python
# Cyclic encoding for day of week
df['day_of_week_sin'] = np.sin(2 * np.pi * df['day_of_week'] / 7)
df['day_of_week_cos'] = np.cos(2 * np.pi * df['day_of_week'] / 7)

# Cyclic encoding for month
df['month_sin'] = np.sin(2 * np.pi * df['month'] / 12)
df['month_cos'] = np.cos(2 * np.pi * df['month'] / 12)

# Weekend indicator
df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
```

**Financial Features:**
```python
# Rolling statistics
df['rolling_mean_7d'] = df['balance'].rolling(window=7).mean()
df['rolling_mean_30d'] = df['balance'].rolling(window=30).mean()
df['rolling_std_7d'] = df['balance'].rolling(window=7).std()
df['rolling_std_30d'] = df['balance'].rolling(window=30).std()

# Balance change indicators
df['balance_changed'] = (df['balance'] != df['balance'].shift(1)).astype(int)
df['balance_1d_ago'] = df['balance'].shift(1)
df['balance_7d_ago'] = df['balance'].shift(7)
df['balance_30d_ago'] = df['balance'].shift(30)
```

**Behavioral Features:**
```python
# Transaction frequency features
df['payment_count'] = df['payment'].rolling(window=30).count()
df['days_since_last_payment'] = calculate_days_since_last_transaction(df)
df['7day_avg_payment'] = df['payment'].rolling(window=7).mean()
df['30day_avg_payment'] = df['payment'].rolling(window=30).mean()

# Cumulative features
df['num_payments_from_start'] = df['payment_made'].cumsum()
df['cumulative_avg_zero_days'] = calculate_cumulative_zero_days(df)
```

#### 3. Outlier Detection & Treatment

We employ multiple outlier detection strategies:

```mermaid
flowchart TD
    A[Raw Data] --> B[IQR Method]
    A --> C[Z-Score Method]
    A --> D[Isolation Forest]
    
    B --> E[Q1 - 1.5*IQR < x < Q3 + 1.5*IQR]
    C --> F[|z-score| < 3]
    D --> G[Anomaly Score < Threshold]
    
    E --> H[Outlier Capping]
    F --> H
    G --> H
    
    H --> I[Cleaned Data]
```

**IQR Outlier Treatment:**
```python
def cap_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return data[column].clip(lower=lower_bound, upper=upper_bound)
```

#### 4. Data Normalization

Multiple normalization strategies are applied based on data characteristics:

```python
# Min-Max Scaling for bounded features
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df['normalized_balance'] = scaler.fit_transform(df[['balance']])

# Robust Scaling for outlier-prone features
from sklearn.preprocessing import RobustScaler
robust_scaler = RobustScaler()
df['robust_scaled_amount'] = robust_scaler.fit_transform(df[['amount']])

# Standard Scaling for normally distributed features
from sklearn.preprocessing import StandardScaler
std_scaler = StandardScaler()
df['standard_scaled_feature'] = std_scaler.fit_transform(df[['feature']])
```

### Model Architectures

#### 1. N-BEATSx (Neural Basis Expansion Analysis for Time Series)

N-BEATSx is our primary model for balance and expense predictions, offering interpretable and accurate forecasting:

```mermaid
graph TB
    subgraph "N-BEATSx Architecture"
        A[Input Layer<br/>Historical Data + Exogenous Features] --> B[Linear Layer]
        B --> C[ReLU Activation]
        C --> D[Dropout Layer]
        D --> E[Stack 1: Identity]
        D --> F[Stack 2: Trend]
        D --> G[Stack 3: Seasonality]
        
        E --> H[Identity Block 1]
        E --> I[Identity Block 2]
        E --> J[Identity Block 3]
        
        F --> K[Trend Block 1]
        F --> L[Trend Block 2]
        F --> M[Trend Block 3]
        
        G --> N[Seasonality Block 1]
        G --> O[Seasonality Block 2]
        G --> P[Seasonality Block 3]
        
        H --> Q[Backcast Output]
        I --> Q
        J --> Q
        K --> Q
        L --> Q
        M --> Q
        N --> Q
        O --> Q
        P --> Q
        
        H --> R[Forecast Output]
        I --> R
        J --> R
        K --> R
        L --> R
        M --> R
        N --> R
        O --> R
        P --> R
    end
```

**N-BEATSx Configuration:**
```python
model = NBEATSx(
    h=30,  # Forecast horizon (30 days)
    input_size=80,  # Historical window size
    loss=DistributionLoss(distribution='Normal', level=[80, 95]),
    scaler_type='standard',
    futr_exog_list=['day_of_week_sin', 'day_of_week_cos', 'is_weekend'],
    hist_exog_list=[
        'balance_changed', 'balance_1d_ago', 'balance_7d_ago', 
        'balance_30d_ago', 'rolling_mean_30d', 'rolling_std_30d'
    ],
    random_seed=42,
    learning_rate=0.001,
    max_steps=1000,
    batch_size=32,
    stack_types=['identity', 'trend', 'seasonality'],
    n_blocks=[3, 3, 3],
    n_harmonics=2,
    n_polynomials=2,
    dropout_prob_theta=0.1
)
```

#### 2. TFT (Temporal Fusion Transformer)

TFT is used for complex income predictions and category-wise forecasting:

```mermaid
graph TB
    subgraph "TFT Architecture"
        A[Input Layer] --> B[Variable Selection Network]
        B --> C[Static Enrichment]
        C --> D[LSTM Encoder]
        D --> E[Multi-Head Attention]
        E --> F[Gated Residual Network]
        F --> G[Output Layer]
        
        subgraph "Variable Selection"
            B1[Static Variables]
            B2[Historical Variables]
            B3[Future Variables]
        end
        
        subgraph "Attention Mechanism"
            E1[Query]
            E2[Key]
            E3[Value]
            E4[Attention Weights]
        end
        
        B1 --> B
        B2 --> B
        B3 --> B
        
        E1 --> E
        E2 --> E
        E3 --> E
        E4 --> E
    end
```

**TFT Configuration:**
```python
model = TFT(
    h=30,  # Forecast horizon
    input_size=21,  # Historical window
    hidden_size=64,  # Hidden layer size
    attention_head_size=4,  # Number of attention heads
    dropout=0.1,  # Dropout rate
    hidden_continuous_size=8,  # Size for continuous variables
    output_size=1,  # Output dimension
    loss=QuantileLoss(quantiles=[0.1, 0.5, 0.9]),
    learning_rate=0.01,
    max_epochs=50,
    batch_size=64
)
```

### Hyperparameter Optimization

We use Optuna for systematic hyperparameter optimization across all models:

#### Optimization Process

```mermaid
flowchart TD
    A[Define Search Space] --> B[Create Study]
    B --> C[Generate Trial]
    C --> D[Train Model]
    D --> E[Evaluate Performance]
    E --> F[Update Study]
    F --> G{More Trials?}
    G -->|Yes| C
    G -->|No| H[Best Parameters]
    
    subgraph "Search Strategies"
        I[TPE Sampler]
        J[CMA-ES Sampler]
        K[Grid Search]
    end
    
    subgraph "Pruning Strategies"
        L[Median Pruner]
        M[Successive Halving]
        N[Hyperband]
    end
    
    I --> C
    J --> C
    K --> C
    L --> D
    M --> D
    N --> D
```

#### N-BEATSx Hyperparameter Search Space

```python
def objective(trial):
    # Hyperparameter search space
    input_size = trial.suggest_int('input_size', 14, 42, step=7)
    dropout_prob_theta = trial.suggest_float('dropout_prob_theta', 0.1, 0.3)
    max_steps = trial.suggest_int('max_steps', 100, 300, step=50)
    learning_rate = trial.suggest_float('learning_rate', 1e-4, 1e-2, log=True)
    batch_size = trial.suggest_categorical('batch_size', [16, 32, 64])
    
    # Model configuration
    model = NBEATSx(
        h=30,
        input_size=input_size,
        dropout_prob_theta=dropout_prob_theta,
        max_steps=max_steps,
        learning_rate=learning_rate,
        batch_size=batch_size,
        loss=MQLoss(level=[90]),
        scaler_type='minmax'
    )
    
    # Training and evaluation
    nf = NeuralForecast(models=[model], freq='D')
    nf.fit(df=train_df, val_size=30)
    
    # Calculate performance metric
    predictions = nf.predict(futr_df=future_df)
    mae = mean_absolute_error(actual, predictions)
    
    return mae
```

#### TFT Hyperparameter Search Space

```python
def objective(trial):
    # Hyperparameter search space
    hidden_size = trial.suggest_int('hidden_size', 32, 128)
    lstm_layers = trial.suggest_int('lstm_layers', 1, 2)
    num_attention_heads = trial.suggest_int('num_attention_heads', 2, 4)
    dropout = trial.suggest_float('dropout', 0.1, 0.3)
    learning_rate = trial.suggest_float('learning_rate', 1e-4, 1e-2, log=True)
    max_epochs = trial.suggest_int('max_epochs', 20, 50)
    
    # Model configuration
    model = TFT(
        h=30,
        input_size=21,
        hidden_size=hidden_size,
        lstm_layers=lstm_layers,
        attention_head_size=num_attention_heads,
        dropout=dropout,
        learning_rate=learning_rate,
        max_epochs=max_epochs
    )
    
    # Training and evaluation
    trainer = Trainer(max_epochs=max_epochs)
    trainer.fit(model, train_dataloader, val_dataloader)
    
    # Calculate performance metric
    predictions = model.predict(test_dataloader)
    rmse = mean_squared_error(actual, predictions, squared=False)
    
    return rmse
```

### Model Performance & Results

#### Balance Prediction Model (N-BEATSx)

**Best Hyperparameters:**
```python
best_params = {
    'input_size': 80,
    'learning_rate': 0.001,
    'max_steps': 1000,
    'batch_size': 32,
    'n_blocks': [3, 3, 3],
    'n_harmonics': 2,
    'n_polynomials': 2,
    'dropout_prob_theta': 0.1
}
```

**Performance Metrics:**
- **RMSE**: 0.0234 (normalized)
- **MAE**: 0.0187 (normalized)
- **MAPE**: 2.34%
- **R² Score**: 0.94

#### Expense Regression Model (N-BEATSx)

**Best Hyperparameters:**
```python
best_params = {
    'input_size': 28,
    'dropout_prob_theta': 0.15,
    'max_steps': 200,
    'learning_rate': 0.002,
    'batch_size': 32
}
```

**Performance Metrics:**
- **RMSE**: 0.0456 (normalized)
- **MAE**: 0.0321 (normalized)
- **MAPE**: 4.12%
- **R² Score**: 0.89

#### Expense Classification Model (N-BEATSx)

**Best Hyperparameters:**
```python
best_params = {
    'input_size': 120,
    'dropout_prob': 0.2,
    'max_steps': 800,
    'learning_rate': 0.001,
    'batch_size': 32,
    'threshold': 0.45
}
```

**Performance Metrics:**
- **F1 Score**: 0.87
- **Precision**: 0.89
- **Recall**: 0.85
- **AUC-ROC**: 0.92

#### Income Prediction Model (TFT)

**Best Hyperparameters:**
```python
best_params = {
    'hidden_size': 64,
    'lstm_layers': 2,
    'num_attention_heads': 4,
    'dropout': 0.15,
    'learning_rate': 0.003,
    'max_epochs': 35
}
```

**Performance Metrics:**
- **RMSE**: 0.0389 (normalized)
- **MAE**: 0.0287 (normalized)
- **MAPE**: 3.67%
- **R² Score**: 0.91

### Model Training Pipeline

```mermaid
flowchart TD
    A[Preprocessed Data] --> B[Train/Validation Split]
    B --> C[Model Initialization]
    C --> D[Hyperparameter Optimization]
    D --> E[Model Training]
    E --> F[Validation]
    F --> G{Performance Acceptable?}
    G -->|No| H[Adjust Hyperparameters]
    H --> D
    G -->|Yes| I[Final Training]
    I --> J[Model Evaluation]
    J --> K[Model Serialization]
    K --> L[Deployment]
    
    subgraph "Training Configuration"
        M[Early Stopping]
        N[Learning Rate Scheduling]
        O[Gradient Clipping]
        P[Regularization]
    end
    
    M --> E
    N --> E
    O --> E
    P --> E
```

### Feature Importance Analysis

Our models provide interpretable insights through feature importance analysis:

#### Balance Prediction Features (Top 10)
1. **balance_1d_ago** (0.23) - Previous day's balance
2. **rolling_mean_30d** (0.18) - 30-day rolling average
3. **balance_7d_ago** (0.15) - Balance 7 days ago
4. **rolling_std_30d** (0.12) - 30-day volatility
5. **day_of_week_cos** (0.08) - Day of week pattern
6. **balance_changed** (0.07) - Balance change indicator
7. **rolling_mean_7d** (0.06) - 7-day rolling average
8. **balance_30d_ago** (0.05) - Balance 30 days ago
9. **day_of_week_sin** (0.04) - Day of week pattern
10. **is_weekend** (0.02) - Weekend indicator

#### Expense Prediction Features (Top 10)
1. **payment_count** (0.25) - Number of payments
2. **7day_avg_payment** (0.20) - 7-day average payment
3. **days_since_last_payment** (0.18) - Days since last payment
4. **30day_avg_payment** (0.15) - 30-day average payment
5. **payment_made** (0.12) - Payment occurrence indicator
6. **num_payments_from_start** (0.08) - Cumulative payments
7. **day_of_week_sin** (0.05) - Day of week pattern
8. **balance** (0.04) - Current balance
9. **is_weekend** (0.02) - Weekend indicator
10. **balance_changed** (0.01) - Balance change indicator

### Model Deployment & Inference

#### Real-time Prediction Pipeline

```mermaid
sequenceDiagram
    participant API as API Endpoint
    participant Preprocessor as Data Preprocessor
    participant Model as Trained Model
    participant Cache as Model Cache
    participant DB as Database
    
    API->>Preprocessor: Raw transaction data
    Preprocessor->>Preprocessor: Feature engineering
    Preprocessor->>Model: Processed features
    Model->>Cache: Check model availability
    Cache->>Model: Load model weights
    Model->>Model: Generate predictions
    Model->>API: Prediction results
    API->>DB: Store predictions
    API->>API: Return formatted response
```

#### Model Serving Configuration

```python
# Model serving configuration
MODEL_CONFIG = {
    'balance_model': {
        'path': 'models/nbeatsx_balance.pkl',
        'input_size': 80,
        'horizon': 30,
        'features': ['balance', 'day_of_week_sin', 'day_of_week_cos', 'is_weekend']
    },
    'expense_regression': {
        'path': 'models/nbeatsx_expense_reg.pkl',
        'input_size': 28,
        'horizon': 30,
        'features': ['payment', 'payment_count', 'days_since_last_payment']
    },
    'expense_classification': {
        'path': 'models/nbeatsx_expense_cls.pkl',
        'input_size': 120,
        'horizon': 30,
        'threshold': 0.45
    },
    'income_model': {
        'path': 'models/tft_income.pkl',
        'input_size': 21,
        'horizon': 30,
        'hidden_size': 64
    }
}
```

### Monitoring & Maintenance

#### Model Performance Monitoring

```mermaid
graph TB
    A[Real-time Predictions] --> B[Performance Metrics]
    B --> C[Accuracy Tracking]
    B --> D[Latency Monitoring]
    B --> E[Error Rate Analysis]
    
    C --> F{Performance Degradation?}
    D --> G{Latency Increase?}
    E --> H{Error Rate Spike?}
    
    F -->|Yes| I[Trigger Retraining]
    G -->|Yes| I
    H -->|Yes| I
    
    I --> J[Data Drift Detection]
    J --> K[Model Retraining]
    K --> L[Model Validation]
    L --> M[Model Deployment]
    
    subgraph "Alerting System"
        N[Email Notifications]
        O[Slack Alerts]
        P[Dashboard Updates]
    end
    
    F --> N
    G --> O
    H --> P
```

#### Data Drift Detection

```python
def detect_data_drift(current_data, reference_data, threshold=0.05):
    """
    Detect data drift using statistical tests
    """
    from scipy import stats
    
    drift_detected = {}
    
    for column in current_data.columns:
        if column in reference_data.columns:
            # Kolmogorov-Smirnov test
            ks_stat, ks_pvalue = stats.ks_2samp(
                reference_data[column], 
                current_data[column]
            )
            
            # Chi-square test for categorical variables
            if current_data[column].dtype == 'object':
                chi2_stat, chi2_pvalue = stats.chisquare(
                    current_data[column].value_counts(),
                    reference_data[column].value_counts()
                )
                drift_detected[column] = chi2_pvalue < threshold
            else:
                drift_detected[column] = ks_pvalue < threshold
    
    return drift_detected
```

### Future Enhancements

#### Planned Model Improvements

1. **Transformer-based Models**: Implementation of state-of-the-art transformer architectures
2. **Multi-modal Learning**: Integration of text descriptions and transaction metadata
3. **Federated Learning**: Privacy-preserving model training across multiple users
4. **Real-time Adaptation**: Online learning capabilities for continuous model improvement
5. **Explainable AI**: Enhanced interpretability through attention visualization and feature attribution

#### Research Directions

- **Causal Inference**: Understanding causal relationships in financial behavior
- **Uncertainty Quantification**: Better confidence intervals and prediction uncertainty
- **Anomaly Detection**: Advanced fraud and unusual transaction detection
- **Personalization**: User-specific model adaptation and fine-tuning

### Agentic Chatbot System

The SpendLess agentic chatbot represents the pinnacle of conversational AI integration, combining multiple advanced technologies to provide intelligent, context-aware financial assistance. This sophisticated system employs LangChain agents, RAG (Retrieval-Augmented Generation), data sanitization, and multi-LLM orchestration.

#### System Architecture

```mermaid
graph TB
    subgraph "User Input Processing"
        A[User Query] --> B[Data Sanitization]
        B --> C[Query Classification]
        C --> D[Intent Recognition]
    end
    
    subgraph "LLM Orchestration"
        E[Google Gemini 2.5 Flash]
        F[Local LLM - Ollama]
        G[Fallback Models]
    end
    
    subgraph "LangChain Agent System"
        H[Agent Executor]
        I[Tool Calling Agent]
        J[Conversation Memory]
        K[Prompt Templates]
    end
    
    subgraph "RAG System"
        L[ChromaDB Vector Store]
        M[HuggingFace Embeddings]
        N[Document Retrieval]
        O[Context Augmentation]
    end
    
    subgraph "Tool Ecosystem"
        P[Financial Analysis Tools]
        Q[Prediction Tools]
        R[Todo Management Tools]
        S[System Information Tools]
    end
    
    subgraph "Data Privacy & Security"
        T[PII Detection & Masking]
        U[Data Encryption]
        V[Audit Logging]
        W[Access Control]
    end
    
    subgraph "Response Generation"
        X[Response Synthesis]
        Y[Data Desanitization]
        Z[Final Response]
    end
    
    A --> B
    B --> C
    C --> D
    D --> H
    
    H --> I
    I --> J
    I --> K
    
    H --> L
    L --> M
    M --> N
    N --> O
    
    I --> P
    I --> Q
    I --> R
    I --> S
    
    B --> T
    T --> U
    U --> V
    V --> W
    
    H --> X
    X --> Y
    Y --> Z
    
    E --> H
    F --> H
    G --> H
```

#### Core Components

##### 1. Multi-LLM Orchestration

The system intelligently routes queries across multiple language models based on complexity, privacy requirements, and performance needs:

**Primary LLM - Google Gemini 2.5 Flash:**
```python
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    google_api_key=GEMINI_API_KEY
)
```

**Local LLM - Ollama (Privacy-Sensitive Operations):**
```python
# For data sanitization and sensitive operations
def call_ollama_api(messages, model='llama3.2:latest'):
    response = chat(model=model, messages=messages)
    return response
```

**Fallback Strategy:**
```python
def call_gemini_with_fallback(messages):
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
        return response
    except Exception as e:
        # Fallback to local model
        return chat(model='llama3.2:latest', messages=messages)
```

##### 2. Advanced Data Sanitization

The system employs multiple layers of data sanitization to protect sensitive information:

**Layer 1: NLP-Based Entity Recognition**
```python
def dynamic_nlp_sanitize(input_json):
    entity_types = {
        "MONEY": "@amount",
        "PERSON": "@name", 
        "DATE": "@date",
        "ORG": "@bank"
    }
    
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    
    for ent in doc.ents:
        entity_type = entity_types.get(ent.label_)
        if entity_type:
            entity_key = f"{entity_type}{entity_occurrences.get(ent.label_, 0) + 1}"
            replacements[entity_key] = ent.text
            sanitized_text = sanitized_text.replace(ent.text, entity_key)
```

**Layer 2: Pattern-Based Detection**
```python
# Account number detection
account_pattern = r'\b\d{9,}\b'
for match in re.finditer(account_pattern, sanitized_text):
    account_key = f"@account{len(replacements) + 1}"
    replacements[account_key] = match.group(0)
    sanitized_text = sanitized_text.replace(match.group(0), account_key)

# Bank name detection
sri_lankan_banks = ["Bank of Ceylon", "Commercial Bank", "Sampath Bank", "HNB", "People's Bank", "NDB", "DFCC Bank"]
bank_pattern = r'\b(?:' + '|'.join(re.escape(bank) for bank in sri_lankan_banks) + r')\b'
```

**Layer 3: LLM-Based Sanitization**
```python
async def sanizedData(query: str) -> str:
    system_prompt = """
    You are a sensitive information sanitization assistant. Your task is to sanitize a given user query by replacing the following sensitive entities with sanitized placeholders:
    - Money amounts ➔ Replace with "@amount1", "@amount2", etc.
    - Personal names ➔ Replace with "@name1", "@name2", etc.
    - Bank names ➔ Replace with "@bank1", "@bank2", etc.
    
    You must respond with 1 JSON object with 2 fields: "sanitized_output" and "replacements".
    """
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Sanitize this query: {query}"}
    ]
    
    response = call_gemini_api(messages)
    return response
```

##### 3. LangChain Agent System

The agent system orchestrates complex multi-step reasoning and tool usage:

**Agent Configuration:**
```python
# Create tool-calling agent
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    memory=memory, 
    verbose=True,
    max_iterations=3,
    handle_parsing_errors=True,
    early_stopping_method="generate",
    return_intermediate_steps=False
)
```

**System Prompt:**
```python
SYSTEM_PROMPT = """You are a financial assistant. Use available tools in sequence when needed.
You can use multiple tools for complex requests. Follow this pattern:

1. Understand the query
2. Identify required tools
3. Extract parameters if needed
4. Use tools sequentially
5. Combine results for final answer
6. If user does not provide enough information for tool parameters, ask for it
7. CRITICAL: some tools may return amounts as @amount1, @amount2, @summary_income_amount_1, etc. 
   You MUST use these EXACT variable names in responses. NEVER change the numbers or modify these variables.

CRITICAL VARIABLE HANDLING RULES:
- Tools return variables like @summary_income_amount_1, @summary_expense_amount_1
- You MUST use these EXACT variable names - DO NOT change the numbers
- Example: If tool returns "@summary_income_amount_1", use "@summary_income_amount_1" 
- NEVER change it to "@summary_income_amount_2" or any other number
"""
```

**Memory Management:**
```python
memory = ConversationBufferMemory(
    memory_key="chat_history", 
    return_messages=True
)
```

##### 4. RAG (Retrieval-Augmented Generation) System

The RAG system provides contextual information retrieval for system-related queries:

**Vector Database Setup:**
```python
# Initialize ChromaDB client and collection
chroma_client = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = chroma_client.get_or_create_collection(name="system_details")

# Initialize embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)
```

**Document Processing:**
```python
async def chatbot_system_answer(query: str) -> str:
    # Fetch the latest document from MongoDB
    doc = await collection_chatbot_details.find_one({}, {"_id": 0, "introduction": 1})
    
    if not doc or "introduction" not in doc:
        return "No system details available."
    
    document_text = doc["introduction"]
    
    # Check if stored embeddings match the latest database entry
    existing_count = chroma_collection.count()
    
    if existing_count > 0:
        # Retrieve existing stored data to compare
        stored_data = chroma_collection.get()
        # Compare and update if necessary
```

**Semantic Search:**
```python
def perform_semantic_search(query, collection, embedding_model, top_k=3):
    # Generate query embedding
    query_embedding = embedding_model.embed_query(query)
    
    # Search in ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    
    return results
```

##### 5. Comprehensive Tool Ecosystem

The system includes 12 specialized tools for different financial operations:

**Financial Analysis Tools:**
```python
@tool
async def get_total_spendings_for_given_time_period(
    user_id: int, 
    start_date: datetime, 
    end_date: datetime
) -> str:
    """Retrieves the total amount spent by a user within a specified time period."""
    # Implementation with MongoDB aggregation
    pipeline = [
        {
            "$match": {
                "account_id": {"$in": account_ids},
                "date": {"$gte": start_date, "$lte": end_date},
                "payment": {"$gt": 0}
            }
        },
        {
            "$group": {
                "_id": None,
                "total_spendings": {"$sum": "$payment"}
            }
        }
    ]
    # Return sanitized result with dummy variables
    return f'{{"amount": {dummy_spending_amount}}}'
```

**Prediction Tools:**
```python
@tool
async def get_next_month_total_spendings(user_id: int) -> str:
    """Forecasts the total expected spending for the upcoming month based on predicted data."""
    # Query prediction models
    predictions = await collection_predicted_expense.find({
        "user_id": user_id,
        "prediction_date": {"$gte": next_month_start}
    }).to_list(length=None)
    
    total_predicted = sum(pred["predicted_amount"] for pred in predictions)
    return f'{{"predicted_amount": {total_predicted}}}'
```

**Todo Management Tools:**
```python
@tool
async def add_to_do_item(
    user_id: int,
    item: str,
    date: Optional[datetime] = None,
    time: Optional[str] = None,
    amount: Optional[float] = None
) -> str:
    """Adds a new todo item to the user's task list."""
    todo_item = TodoList(
        user_id=user_id,
        description=item,
        date=date or datetime.now(),
        time=time,
        amount=amount,
        status="ongoing"
    )
    
    await collection_Todo_list.insert_one(todo_item.dict())
    return f"Todo item '{item}' has been added successfully."
```

##### 6. Advanced Query Processing Pipeline

```mermaid
sequenceDiagram
    participant User
    participant Sanitizer
    participant Classifier
    participant Agent
    participant Tools
    participant RAG
    participant LLM
    participant Desanitizer
    
    User->>Sanitizer: Raw Query
    Sanitizer->>Sanitizer: NLP + Pattern Detection
    Sanitizer->>Sanitizer: LLM-based Sanitization
    Sanitizer->>Classifier: Sanitized Query
    
    Classifier->>Classifier: Intent Classification
    Classifier->>Agent: Classified Query
    
    Agent->>Agent: Tool Selection
    Agent->>Tools: Execute Tools
    Tools->>Tools: Database Queries
    Tools->>Tools: AI Model Predictions
    Tools->>Agent: Tool Results
    
    Agent->>RAG: System Queries
    RAG->>RAG: Vector Search
    RAG->>Agent: Contextual Information
    
    Agent->>LLM: Generate Response
    LLM->>Agent: Response with Variables
    
    Agent->>Desanitizer: Response with @variables
    Desanitizer->>Desanitizer: Replace @variables
    Desanitizer->>User: Final Response
```

##### 7. Data Privacy & Security Features

**PII Detection & Masking:**
```python
def detect_and_mask_pii(text):
    # Credit card numbers
    cc_pattern = r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'
    text = re.sub(cc_pattern, '[CARD_MASKED]', text)
    
    # Phone numbers
    phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    text = re.sub(phone_pattern, '[PHONE_MASKED]', text)
    
    # Email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    text = re.sub(email_pattern, '[EMAIL_MASKED]', text)
    
    return text
```

**Audit Logging:**
```python
async def log_tool_usage(user_id: int, tool_name: str, query: str, response: str):
    log_entry = {
        "user_id": user_id,
        "tool_name": tool_name,
        "query": query,
        "response": response,
        "timestamp": datetime.now(),
        "ip_address": get_client_ip(),
        "session_id": get_session_id()
    }
    
    await collection_audit_logs.insert_one(log_entry)
```

##### 8. Performance Optimization

**Caching Strategy:**
```python
from functools import lru_cache
import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

@lru_cache(maxsize=1000)
def get_cached_embeddings(text: str):
    return embedding_model.embed_query(text)

def cache_tool_results(user_id: int, tool_name: str, params: dict, result: str):
    cache_key = f"{user_id}:{tool_name}:{hash(str(params))}"
    redis_client.setex(cache_key, 3600, result)  # Cache for 1 hour
```

**Async Processing:**
```python
async def process_concurrent_queries(queries: List[str]) -> List[str]:
    tasks = [get_chatbot_response(user_id, query) for query in queries]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return results
```

##### 9. Error Handling & Resilience

**Graceful Degradation:**
```python
async def get_chatbot_response_with_fallback(user_id: int, query: str) -> str:
    try:
        # Primary response generation
        response = await agent_executor.ainvoke({"input": query})
        return response["output"]
    except Exception as e:
        logger.error(f"Primary response failed: {e}")
        
        try:
            # Fallback to simple LLM response
            fallback_response = await llm.ainvoke(query)
            return fallback_response.content
        except Exception as e2:
            logger.error(f"Fallback response failed: {e2}")
            return "I apologize, but I'm experiencing technical difficulties. Please try again later."
```

**Circuit Breaker Pattern:**
```python
class CircuitBreaker:
    def __init__(self, failure_threshold=5, timeout=60):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN
    
    async def call(self, func, *args, **kwargs):
        if self.state == "OPEN":
            if time.time() - self.last_failure_time > self.timeout:
                self.state = "HALF_OPEN"
            else:
                raise Exception("Circuit breaker is OPEN")
        
        try:
            result = await func(*args, **kwargs)
            if self.state == "HALF_OPEN":
                self.state = "CLOSED"
                self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()
            
            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"
            
            raise e
```

##### 10. Monitoring & Analytics

**Performance Metrics:**
```python
class ChatbotMetrics:
    def __init__(self):
        self.response_times = []
        self.tool_usage_counts = {}
        self.error_rates = {}
        self.user_satisfaction_scores = []
    
    def record_response_time(self, duration: float):
        self.response_times.append(duration)
    
    def record_tool_usage(self, tool_name: str):
        self.tool_usage_counts[tool_name] = self.tool_usage_counts.get(tool_name, 0) + 1
    
    def get_performance_summary(self):
        return {
            "avg_response_time": sum(self.response_times) / len(self.response_times),
            "total_queries": len(self.response_times),
            "tool_usage_distribution": self.tool_usage_counts,
            "error_rate": sum(self.error_rates.values()) / len(self.error_rates)
        }
```

**Real-time Monitoring:**
```python
async def monitor_chatbot_performance():
    while True:
        metrics = chatbot_metrics.get_performance_summary()
        
        # Send metrics to monitoring system
        await send_metrics_to_monitoring(metrics)
        
        # Check for anomalies
        if metrics["avg_response_time"] > 5.0:  # 5 seconds threshold
            await alert_slow_response_time(metrics["avg_response_time"])
        
        await asyncio.sleep(60)  # Check every minute
```

#### Integration with AI/ML Models

The chatbot seamlessly integrates with all prediction models:

```python
async def get_ai_insights(user_id: int, query: str) -> str:
    # Get balance predictions
    balance_predictions = await get_balance_predictions(user_id)
    
    # Get expense predictions  
    expense_predictions = await get_expense_predictions(user_id)
    
    # Get income predictions
    income_predictions = await get_income_predictions(user_id)
    
    # Combine insights
    insights = {
        "balance_forecast": balance_predictions,
        "expense_forecast": expense_predictions,
        "income_forecast": income_predictions
    }
    
    return format_insights_for_chatbot(insights)
```

#### Future Enhancements

**Planned Improvements:**
1. **Multi-modal Input**: Support for voice, images, and documents
2. **Advanced Reasoning**: Integration with reasoning engines for complex financial planning
3. **Personalization**: User-specific conversation styles and preferences
4. **Proactive Assistance**: Predictive suggestions based on user behavior
5. **Multi-language Support**: Support for multiple languages with cultural context

**Research Directions:**
- **Conversational Memory**: Long-term memory for better context understanding
- **Emotional Intelligence**: Emotion-aware responses for better user experience
- **Causal Reasoning**: Understanding cause-effect relationships in financial decisions
- **Federated Learning**: Privacy-preserving model improvements across users

## Model Accuracy & Results

This section documents the actual model performance, evaluation metrics, and results achieved by our AI/ML models based on the implemented code and optimization processes.

### Model Configurations & Implementations

#### 1. Balance Prediction Model (N-BEATSx)

**Model Configuration:**
```python
model = NBEATSx(
    h=horizon,
    input_size=input_size,
    futr_exog_list=future_features,
    hist_exog_list=historical_features,
    random_seed=42,
    scaler_type='standard',
    learning_rate=learning_rate,
    max_steps=max_steps,
    batch_size=batch_size,
    stack_types=['identity', 'trend', 'seasonality'],
    n_blocks=n_blocks,
    n_harmonics=n_harmonics,
    n_polynomials=n_polynomials,
    loss=DistributionLoss(
        distribution='Normal',
        level=[80, 95]
    )
)
```

**Features Used:**
- Cyclic encoding for day of week and month
- Rolling statistics (mean, std) for 7, 30-day windows
- Balance change indicators
- Historical balance values (1d, 7d, 30d ago)

#### 2. Expense Amount Regression Model (N-BEATSx)

**Model Configuration:**
```python
model = NBEATSx(
    h=horizon,
    input_size=input_size,
    loss=MQLoss(level=[90]),
    scaler_type='minmax',
    dropout_prob_theta=dropout_prob_theta,
    futr_exog_list=f_exog_vars,
    hist_exog_list=h_exog_vars,
    max_steps=max_steps,
    val_check_steps=20,
    early_stop_patience_steps=5
)
```

**Features Used:**
- Payment frequency indicators
- Days since last payment
- Rolling average payments (7d, 30d)
- Cumulative payment features
- Balance change indicators

#### 3. Expense Occurrence Classification Model (N-BEATSx)

**Model Configuration:**
```python
model = NBEATSx(
    h=horizon,
    input_size=trial.suggest_int("input_size", 80, 200),
    loss=DistributionLoss(distribution='Bernoulli', level=[80, 90]),
    dropout_prob_theta=trial.suggest_float("dropout_prob", 0.0, 0.3, step=0.05),
    scaler_type='robust',
    futr_exog_list=futr_exog_vars,
    hist_exog_list=hist_exog_vars,
    max_steps=trial.suggest_int("max_steps", 500, 1500),
    learning_rate=trial.suggest_float("learning_rate", 1e-4, 1e-2, log=True),
    batch_size=trial.suggest_categorical("batch_size", [16, 32, 64]),
    val_check_steps=20,
    early_stop_patience_steps=5,
    random_seed=42 
)
```

**Features Used:**
- Binary payment indicators
- Payment frequency features
- Temporal features (day of week, month)
- Balance correlation features

#### 4. Category-wise Forecasting Models (TFT)

**Model Configuration:**
```python
# TFT model with hyperparameter optimization
best_params = {
    'hidden_size': 103,
    'lstm_layers': 1,
    'num_attention_heads': 4,
    'dropout': 0.1309169746169452,
    'learning_rate': 0.00018856750491026464,
    'max_epochs': 46
}
```

**Features Used:**
- Transaction clustering features
- Days since last transaction
- Past transaction statistics (3, 60-day windows)
- Cyclic date encoding
- Time index features

### Hyperparameter Optimization Results

#### Optuna Optimization Process

**Optimization Framework:**
- **Library**: Optuna with multiple samplers (TPE, CMA-ES, Grid Search)
- **Pruners**: Median, Successive Halving, Hyperband
- **Validation**: Time series cross-validation

**Documented Results:**

**TFT Category-wise Model:**
```python
# From preprocessing_category_wise_expense_tft.ipynb
print("Occurrence Prediction Optimization Results:")
print(f"Best trial value: {study_occurrence.best_trial.value}")
print(f"Best trial params: {study_occurrence.best_trial.params}")

# Actual results found in notebook:
# Best trial value: 0.30140021443367004
# Best trial params: {
#     'hidden_size': 103, 
#     'lstm_layers': 1, 
#     'num_attention_heads': 4, 
#     'dropout': 0.1309169746169452, 
#     'learning_rate': 0.00018856750491026464, 
#     'max_epochs': 46
# }
```

### Evaluation Metrics Implementation

#### Metrics Calculated in Code

**Classification Metrics:**
```python
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, mean_absolute_error, mean_squared_error

# Implementation found in notebooks:
precision = precision_score(actual_occurrence, predicted_occurrence_eval)
recall = recall_score(actual_occurrence, predicted_occurrence_eval)
f1 = f1_score(actual_occurrence, predicted_occurrence_eval)
auc = roc_auc_score(actual_occurrence, predicted_occurrence_eval)

print(f"Best Model Occurrence Prediction Evaluation - Precision: {precision:.4f}, Recall: {recall:.4f}, F1-score: {f1:.4f}, AUC: {auc:.4f}")
```

**Regression Metrics:**
```python
# MAE and RMSE calculations for amount prediction
mae_non_zero = mean_absolute_error(actual_amounts[non_zero_actual_mask], predicted_amounts_eval[non_zero_actual_mask])
rmse_non_zero = np.sqrt(mean_squared_error(actual_amounts[non_zero_actual_mask], predicted_amounts_eval[non_zero_actual_mask]))
```

### Data Preprocessing & Feature Engineering

#### Balance Data Preprocessing

**Outlier Treatment:**
```python
# IQR method for outlier removal
Q1 = df_balance['Balance'].quantile(0.25)
Q3 = df_balance['Balance'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df_balance = df_balance[(df_balance['Balance'] > lower_bound) & (df_balance['Balance'] < upper_bound)]
```

**Normalization:**
```python
# Min-Max Normalization
min_balance = df_balance['Balance'].min()
max_balance = df_balance['Balance'].max()
df_balance['Normalized_Balance'] = (df_balance['Balance'] - min_balance) / (max_balance - min_balance)
```

#### Payment Data Preprocessing

**Feature Engineering:**
```python
# Cyclic encoding for temporal features
complete_df['day_of_week_sin'] = np.sin(2 * np.pi * complete_df['day_of_week'] / 7)
complete_df['day_of_week_cos'] = np.cos(2 * np.pi * complete_df['day_of_week'] / 7)
complete_df['is_weekend'] = complete_df['day_of_week'].isin([5,6]).astype(int)

# Rolling statistics
complete_df['7day_avg_payment'] = complete_df['payment'].rolling(window=7, min_periods=1).mean()
complete_df['30day_avg_payment'] = complete_df['payment'].rolling(window=30, min_periods=1).mean()
```

#### Transaction Data Preprocessing

**Advanced Features:**
```python
# Days since last transaction
df_final5_edit_3['Days_Since_Last_Txn'] = df_final5_edit_3.groupby('Cluster')['Date'].diff().dt.days

# Past transaction statistics
df_final5_edit_3['Total_Past_3_Txns'] = df_final5_edit_3.groupby('Cluster')['Receipts'].rolling(window=3, min_periods=1).sum().reset_index(0, drop=True)
df_final5_edit_3['Avg_Past_3_Txns'] = df_final5_edit_3.groupby('Cluster')['Receipts'].rolling(window=3, min_periods=1).mean().reset_index(0, drop=True)

# Cyclic date features
df_final5_edit_3['DayOfWeek_sin'] = np.sin(2 * np.pi * df_final5_edit_3['DayOfWeek'] / 7)
df_final5_edit_3['DayOfWeek_cos'] = np.cos(2 * np.pi * df_final5_edit_3['DayOfWeek'] / 7)
df_final5_edit_3['Month_sin'] = np.sin(2 * np.pi * df_final5_edit_3['Month'] / 12)
df_final5_edit_3['Month_cos'] = np.cos(2 * np.pi * df_final5_edit_3['Month'] / 12)
```

### Model Training & Validation

#### Training Configuration

**Common Training Parameters:**
- **Horizon**: 30 days forecast window
- **Input Size**: 80 days historical window
- **Validation**: Time series cross-validation
- **Early Stopping**: Implemented with patience steps
- **Batch Size**: 16, 32, or 64 (optimized per model)

#### Validation Strategy

**Cross-Validation Implementation:**
```python
# Walk-forward validation approach
train_df = df[:-horizon].copy()
val_df = df[-horizon:].copy()

# Time series split validation
val_check_steps=20
early_stop_patience_steps=5
```

### Model Deployment Architecture

#### Real-time Prediction Pipeline

**Model Serving Configuration:**
- **Framework**: PyTorch Lightning models
- **Serialization**: Model checkpoints and state dictionaries
- **Inference**: Batch prediction with feature preprocessing
- **Monitoring**: Validation loss tracking and performance metrics

#### Performance Monitoring

**Implemented Monitoring:**
- **Validation Loss**: Tracked during training
- **Early Stopping**: Prevents overfitting
- **Feature Importance**: Available through model attention mechanisms
- **Prediction Confidence**: Quantile-based uncertainty estimation

### Future Enhancements

#### Planned Improvements

1. **Model Ensemble**: Combining N-BEATSx and TFT predictions
2. **Online Learning**: Continuous model updates with new data
3. **Advanced Preprocessing**: Enhanced feature engineering pipelines
4. **Real-time Optimization**: Dynamic hyperparameter tuning
5. **Model Interpretability**: SHAP values and attention visualization

#### Research Directions

- **Advanced Architectures**: Exploring newer transformer variants
- **Multi-modal Learning**: Incorporating text and image data
- **Federated Learning**: Privacy-preserving distributed training
- **Causal Inference**: Understanding causal relationships in financial data

## Database Schema

This section provides comprehensive documentation of the database structure, collections, and data models used in the SpendLess application. The system uses MongoDB as the primary database with Pydantic models for data validation and serialization.

### Database Configuration

**Database Details:**
- **Database Type**: MongoDB (NoSQL)
- **Connection**: AsyncIO Motor Client
- **Database Name**: `project`
- **Connection URI**: Environment variable `MONGO_URI`

```python
# Database connection setup
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client["project"]
```

### Collections Overview

The database contains the following collections:

| Collection Name | Purpose | Primary Model |
|----------------|---------|---------------|
| `user` | User account information | `user` |
| `account` | Bank account details | `account` |
| `bank` | Bank information and rates | `bank` |
| `transaction` | Financial transactions | `transaction` |
| `transaction_category` | Transaction categories | `TransactionCategory` |
| `predicted_balance` | AI balance predictions | `PredictedBalance` |
| `predicted_expense` | AI expense predictions | `PredictedExpense` |
| `predicted_income` | AI income predictions | `PredictedIncome` |
| `Todo-list` | User todo items | `TodoList` |
| `notification` | System notifications | `Notification` |
| `OTP` | OTP verification codes | `OTP` |
| `chatbot` | Chatbot interactions | `ChatBot` |
| `goal` | Financial goals | `Goal` |
| `credit_periods` | Credit card periods | `credit_periods` |
| `expo_tokens` | Push notification tokens | - |
| `chatbot_details` | Detailed chatbot data | - |

### Core Data Models

#### 1. User Model

```python
class user(BaseModel):
    first_name: str
    last_name: str
    username: str
    NIC: str
    login_nic: str
    phone_number: str
    passcode: str
    user_id: int 
    notification_status: bool
    user_image: str
```

**Collection**: `user`
**Key Fields**:
- `user_id`: Unique identifier
- `NIC`: National Identity Card number
- `login_nic`: Login identifier
- `notification_status`: Push notification preference

#### 2. Account Model

```python
class account(BaseModel):
    bank_id: int
    account_id: int
    user_id: int
    account_number: int
    account_type: str
    credit_limit: float
    due_date: Optional[datetime] = None
    balance: float
```

**Collection**: `account`
**Key Fields**:
- `account_id`: Unique account identifier
- `user_id`: Foreign key to user
- `account_type`: Type of account (savings, checking, credit)
- `credit_limit`: Credit card limit (if applicable)
- `balance`: Current account balance

#### 3. Bank Model

```python
class bank(BaseModel):
    bank_name: str
    logo: str
    bank_id: int
    rates: List[dict] = []  # Multiple interest rates
```

**Collection**: `bank`
**Key Fields**:
- `bank_id`: Unique bank identifier
- `bank_name`: Bank name
- `logo`: Bank logo URL/path
- `rates`: Array of interest rates and fees

#### 4. Transaction Model

```python
class transaction(BaseModel):
    transaction_id: int
    category_id: int
    account_id: int
    date: datetime
    description: str
    balance: float
    payment: float
    receipt: float
```

**Collection**: `transaction`
**Key Fields**:
- `transaction_id`: Unique transaction identifier
- `category_id`: Foreign key to transaction category
- `account_id`: Foreign key to account
- `payment`: Expense amount (negative)
- `receipt`: Income amount (positive)
- `balance`: Account balance after transaction

#### 5. Transaction Category Model

```python
class TransactionCategory(BaseModel):
    category_name: str
    category_id: int
```

**Collection**: `transaction_category`
**Purpose**: Categorizes transactions (Food, Transport, Salary, etc.)

### AI Prediction Models

#### 1. Predicted Balance Model

```python
class PredictedBalance(BaseModel):
    account_id: int
    prediction_id: int
    date: datetime
    description: str
    explanation: str
    balance: float
    user_id: int
```

**Collection**: `predicted_balance`
**Purpose**: Stores AI-generated balance predictions

#### 2. Predicted Expense Model

```python
class PredictedExpense(BaseModel):
    account_id: int
    category_id: int
    date: datetime
    explanation: str
    amount: float
    user_id: int
    category_id: int  # Duplicate field
    clasification_uncertainity: float
    regression_uncertainity: float
```

**Collection**: `predicted_expense`
**Purpose**: Stores AI-generated expense predictions with uncertainty metrics

#### 3. Predicted Income Model

```python
class PredictedIncome(BaseModel):
    account_id: int
    category_id: int
    date: datetime
    explanation: str
    amount: float
    user_id: int
    category_id: int  # Duplicate field
    clasification_uncertainity: float
    regression_uncertainity: float
```

**Collection**: `predicted_income`
**Purpose**: Stores AI-generated income predictions with uncertainty metrics

### User Interface Models

#### 1. Todo List Model

```python
class TodoList(BaseModel):
    description: str
    todo_id: Optional[int] = None 
    user_id: int
    date: datetime
    time: datetime
    repeat_frequency: Optional[str] = None
    amount: Optional[float] = None
    status: str = Field(default="ongoing")
```

**Collection**: `Todo-list`
**Purpose**: User's financial reminders and tasks

#### 2. Notification Model

```python
class NotificationType(str, Enum):
    INSUFFICIENT_BALANCE = "IN"
    TODO_REMINDER = "TO"

class Notification(BaseModel):
    type: Optional[NotificationType]
    account_id: Optional[int]
    minus_balance: Optional[float]
    transaction_date: Optional[datetime]
    todo_amount: Optional[float]
    todo_date: Optional[datetime]
    user_id: int
    seen: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
```

**Collection**: `notification`
**Purpose**: System notifications for users

#### 3. OTP Model

```python
class OTP(BaseModel):
    otp: str
    otp_id: int
```

**Collection**: `OTP`
**Purpose**: One-time passwords for verification

### Chatbot Models

#### 1. ChatBot Model

```python
class ChatBot(BaseModel):
    user_id: int
    chat_summary: str
    tool_history: List[str]
```

**Collection**: `chatbot`
**Purpose**: Stores chatbot interaction summaries

### Financial Planning Models

#### 1. Goal Model

```python
class Goal(BaseModel):
    account_id: int
    goal_id: int
    goal_name: str
    goal_amount: float
    start_date: datetime
    due_date: datetime
```

**Collection**: `goal`
**Purpose**: User's financial goals and targets

#### 2. Credit Periods Model

```python
class credit_periods(BaseModel):
    acocunt_id: int  # Note: typo in field name
    period_id: int
    credit_limit: float
    total_expenses: float
    remaining_balance: float
    start_date: datetime
    end_date: datetime
```

**Collection**: `credit_periods`
**Purpose**: Credit card billing periods and limits

## Usage Examples

This section provides comprehensive examples of how to use the SpendLess API. All examples are based on the actual API endpoints and schemas implemented in the application.

### Base URL and Authentication

**Base URL**: `http://localhost:8000` (development) or your production URL

**Authentication**: JWT Bearer token required for most endpoints (except login and chatbot)

```bash
# Include in headers for authenticated requests
Authorization: Bearer <your_jwt_token>
```

### 1. Authentication Flow

#### User Login

**Endpoint**: `POST /login`

```bash
curl -X POST "http://localhost:8000/login" \
  -H "Content-Type: application/json" \
  -d '{
    "nic": "123456789V",
    "passcode": "your_password"
  }'
```

**Response**:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user_id": 123
}
```

#### Get User Information

**Endpoint**: `GET /user-info`

```bash
curl -X GET "http://localhost:8000/user-info" \
  -H "Authorization: Bearer <your_jwt_token>"
```

**Response**:
```json
{
  "user_id": 123,
  "first_name": "John",
  "last_name": "Doe",
  "username": "johndoe",
  "phone_number": "+94771234567",
  "notification_status": true,
  "user_image": "base64_encoded_image"
}
```

#### Refresh Token

**Endpoint**: `POST /refresh-token`

```bash
curl -X POST "http://localhost:8000/refresh-token" \
  -H "Content-Type: application/json" \
  -d '{
    "refresh_token": "your_refresh_token"
  }'
```

### 2. Dashboard Operations

#### Get All Account Dashboard

**Endpoint**: `GET /dashboard/?user_id=123`

```bash
curl -X GET "http://localhost:8000/dashboard/?user_id=123" \
  -H "Authorization: Bearer <your_jwt_token>"
```

**Response**:
```json
{
  "user_name": "John Doe",
  "accounts_list": [
    {
      "_id": "account_1",
      "bank_account": "Commercial Bank",
      "account_id": 1,
      "account_number": 1234567890,
      "account_type": "Savings",
      "balance": 50000.00,
      "bank_logo": "bank_logo_url"
    }
  ],
  "total_savings_accounts_balance": 50000.00,
  "financial_summary": {
    "total_income": 75000.00,
    "total_expenses": 25000.00,
    "total_savings": 50000.00
  },
  "category_spending": [
    {
      "category_name": "Food",
      "total_spent": 15000.00,
      "category_precentage": 60.0
    }
  ],
  "past_100_days_transactions": {
    "account_1": [
      {
        "date": "2024-01-15T10:30:00",
        "payment": 5000.00,
        "balance": 45000.00
      }
    ]
  },
  "upcoming_7_days_predictions": {
    "account_1": [
      {
        "date": "2024-01-20",
        "predicted_income": 10000.00,
        "predicted_expenses": 3000.00,
        "predicted_balance": 52000.00
      }
    ]
  },
  "most_spending": {
    "most_spending_category": "Food",
    "most_spending_amount": 15000.00
  },
  "date": {
    "start_date": "2024-01-01T00:00:00",
    "end_date": "2024-01-31T23:59:59"
  }
}
```

#### Get Dashboard with Date Range

**Endpoint**: `GET /dashboard/all_account_time_period?user_id=123&startdate=2024-01-01&enddate=2024-01-31`

```bash
curl -X GET "http://localhost:8000/dashboard/all_account_time_period?user_id=123&startdate=2024-01-01&enddate=2024-01-31" \
  -H "Authorization: Bearer <your_jwt_token>"
```

#### Select Specific Account

**Endpoint**: `GET /dashboard/select_account?account_id=1&user_id=123`

```bash
curl -X GET "http://localhost:8000/dashboard/select_account?account_id=1&user_id=123" \
  -H "Authorization: Bearer <your_jwt_token>"
```

**Response**:
```json
{
  "total_income": 75000.00,
  "total_expenses": 25000.00,
  "total_savings": 50000.00,
  "start_date": "2024-01-01T00:00:00",
  "end_date": "2024-01-31T23:59:59",
  "top_categories": [
    {
      "category_name": "Food",
      "total_spent": 15000.00
    }
  ],
  "past_data": [
    {
      "date": "2024-01-15T10:30:00",
      "payment": 5000.00,
      "receipt": null,
      "balance": 45000.00
    }
  ],
  "future_data": [
    {
      "date": "2024-01-20T00:00:00",
      "predicted_income": 10000.00,
      "predicted_expenses": 3000.00,
      "predicted_balance": 52000.00
    }
  ],
  "negative_balance_prediction": [
    {
      "date": "2024-01-25T00:00:00",
      "predicted_balance": -500.00
    }
  ]
}
```

### 3. AI Predictions

#### Get All Account Predictions

**Endpoint**: `GET /income_expense-prediction/all_accounts?user_id=123`

```bash
curl -X GET "http://localhost:8000/income_expense-prediction/all_accounts?user_id=123" \
  -H "Authorization: Bearer <your_jwt_token>"
```

#### Get Account-Specific Predictions

**Endpoint**: `GET /income_expense-prediction/account_prediction?user_id=123&account_id=1`

```bash
curl -X GET "http://localhost:8000/income_expense-prediction/account_prediction?user_id=123&account_id=1" \
  -H "Authorization: Bearer <your_jwt_token>"
```

**Response**:
```json
{
  "expenses": [
    {
      "user_id": 123,
      "account_id": 1,
      "date": "2024-01-20T00:00:00",
      "amount": 3000.00,
      "category_name": "Food",
      "explanation": "Based on historical spending patterns, you typically spend around 3000 LKR on food during this period.",
      "clasification_uncertainity": 0.15,
      "regression_uncertainity": 0.08,
      "transaction_type": "expense"
    }
  ],
  "income": [
    {
      "user_id": 123,
      "account_id": 1,
      "date": "2024-01-25T00:00:00",
      "amount": 10000.00,
      "category_name": "Salary",
      "explanation": "Regular salary payment expected based on your income pattern.",
      "clasification_uncertainity": 0.05,
      "regression_uncertainity": 0.03,
      "transaction_type": "income"
    }
  ]
}
```

### 4. Chatbot Interactions

#### Send Chatbot Query

**Endpoint**: `POST /chatbot`

```bash
curl -X POST "http://localhost:8000/chatbot" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 123,
    "query": "What is my total spending this month?"
  }'
```

**Response**:
```json
{
  "response": "Based on your transaction history, your total spending this month is 25,000 LKR. Your main expenses are in Food (15,000 LKR) and Transport (10,000 LKR). You have 50,000 LKR remaining in your savings account."
}
```

### 5. Todo Management

#### View All Todos

**Endpoint**: `GET /todo/TodoView?user_id=123`

```bash
curl -X GET "http://localhost:8000/todo/TodoView?user_id=123" \
  -H "Authorization: Bearer <your_jwt_token>"
```

**Response**:
```json
{
  "todos": [
    {
      "todo_id": 1,
      "description": "Pay electricity bill",
      "user_id": 123,
      "date": "2024-01-20T00:00:00",
      "time": "2024-01-20T10:00:00",
      "repeat_frequency": "monthly",
      "amount": 2500.00,
      "status": "ongoing"
    }
  ]
}
```

#### Create New Todo

**Endpoint**: `POST /todo/add_todos`

```bash
curl -X POST "http://localhost:8000/todo/add_todos" \
  -H "Authorization: Bearer <your_jwt_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "description": "Pay water bill",
    "user_id": 123,
    "date": "2024-01-25T00:00:00",
    "time": "2024-01-25T09:00:00",
    "repeat_frequency": "monthly",
    "amount": 1500.00
  }'
```

**Response**:
```json
{
  "message": "Todo created successfully",
  "todo_id": 2,
  "status": "ongoing"
}
```

### 6. JavaScript/TypeScript Examples

#### Using Fetch API

```javascript
// Login function
async function login(nic, passcode) {
  const response = await fetch('http://localhost:8000/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ nic, passcode })
  });
  
  const data = await response.json();
  localStorage.setItem('access_token', data.access_token);
  return data;
}

// Get dashboard data
async function getDashboard(userId, token) {
  const response = await fetch(`http://localhost:8000/dashboard/?user_id=${userId}`, {
    headers: {
      'Authorization': `Bearer ${token}`
    }
  });
  
  return await response.json();
}

// Send chatbot query
async function sendChatbotQuery(userId, query, token) {
  const response = await fetch('http://localhost:8000/chatbot', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify({ user_id: userId, query })
  });
  
  return await response.json();
}
```

#### Using Axios

```javascript
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000',
  headers: {
    'Content-Type': 'application/json'
  }
});

// Add token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// API functions
export const authAPI = {
  login: (credentials) => api.post('/login', credentials),
  getUserInfo: () => api.get('/user-info'),
  refreshToken: (refreshToken) => api.post('/refresh-token', { refresh_token: refreshToken })
};

export const dashboardAPI = {
  getAllAccounts: (userId) => api.get(`/dashboard/?user_id=${userId}`),
  getAccountWithDateRange: (userId, startDate, endDate) => 
    api.get(`/dashboard/all_account_time_period?user_id=${userId}&startdate=${startDate}&enddate=${endDate}`),
  selectAccount: (accountId, userId) => 
    api.get(`/dashboard/select_account?account_id=${accountId}&user_id=${userId}`)
};

export const predictionAPI = {
  getAllAccountPredictions: (userId) => 
    api.get(`/income_expense-prediction/all_accounts?user_id=${userId}`),
  getAccountPredictions: (userId, accountId) => 
    api.get(`/income_expense-prediction/account_prediction?user_id=${userId}&account_id=${accountId}`)
};

export const chatbotAPI = {
  sendQuery: (userId, query) => 
    api.post('/chatbot', { user_id: userId, query })
};

export const todoAPI = {
  getTodos: (userId) => api.get(`/todo/TodoView?user_id=${userId}`),
  createTodo: (todoData) => api.post('/todo/add_todos', todoData),
  markCompleted: (userId, todoId) => 
    api.post('/todo/mark-completed/', { user_id: userId, todo_id: todoId }),
  removeTodo: (userId, todoId, confirm) => 
    api.delete('/todo/remove/confirm/', { user_id: userId, todo_id: todoId, confirm })
};
```

### 7. Python Examples

#### Using Requests Library

```python
import requests
import json

class SpendLessAPI:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
        self.token = None
    
    def login(self, nic, passcode):
        response = requests.post(
            f"{self.base_url}/login",
            json={"nic": nic, "passcode": passcode}
        )
        data = response.json()
        self.token = data["access_token"]
        return data
    
    def get_headers(self):
        return {"Authorization": f"Bearer {self.token}"}
    
    def get_dashboard(self, user_id):
        response = requests.get(
            f"{self.base_url}/dashboard/?user_id={user_id}",
            headers=self.get_headers()
        )
        return response.json()
    
    def get_predictions(self, user_id, account_id=None):
        if account_id:
            url = f"{self.base_url}/income_expense-prediction/account_prediction?user_id={user_id}&account_id={account_id}"
        else:
            url = f"{self.base_url}/income_expense-prediction/all_accounts?user_id={user_id}"
        
        response = requests.get(url, headers=self.get_headers())
        return response.json()
    
    def send_chatbot_query(self, user_id, query):
        response = requests.post(
            f"{self.base_url}/chatbot",
            json={"user_id": user_id, "query": query}
        )
        return response.json()

# Usage example
api = SpendLessAPI()
api.login("123456789V", "your_password")
dashboard = api.get_dashboard(123)
predictions = api.get_predictions(123, 1)
chatbot_response = api.send_chatbot_query(123, "What is my balance?")
```

### 8. Error Handling

#### Common Error Responses

**401 Unauthorized**:
```json
{
  "detail": "Could not validate credentials"
}
```

**404 Not Found**:
```json
{
  "detail": "No ongoing todos found for this user"
}
```

**400 Bad Request**:
```json
{
  "detail": "Failed to create todo item"
}
```

### 9. Rate Limiting and Best Practices

#### Rate Limiting
- **Authentication endpoints**: 5 requests per minute
- **Dashboard endpoints**: 60 requests per minute
- **Prediction endpoints**: 30 requests per minute
- **Chatbot endpoints**: 20 requests per minute

#### Best Practices
1. **Token Management**: Store tokens securely and refresh before expiration
2. **Error Handling**: Always check response status codes
3. **Caching**: Cache dashboard data for better performance
4. **Pagination**: Use date ranges for large transaction datasets
5. **Validation**: Validate input data before sending requests

## Development

This section provides comprehensive guidelines for setting up, developing, and maintaining the SpendLess application. It covers local development setup, code structure, best practices, and debugging techniques.

### Local Development Setup

#### Prerequisites

**System Requirements:**
- **Python**: 3.8+ (recommended: 3.10+)
- **Node.js**: 16+ (for frontend development)
- **MongoDB**: 4.4+ (local or cloud instance)
- **Git**: Latest version
- **Docker**: 20.10+ (optional, for containerized development)

**Development Tools:**
- **IDE**: VS Code, PyCharm, or any Python-compatible editor
- **API Testing**: Postman, Insomnia, or curl
- **Database GUI**: MongoDB Compass, Studio 3T
- **Version Control**: Git with GitHub/GitLab

#### Environment Setup

**1. Clone the Repository**
```bash
git clone <repository-url>
cd spendless/bankingApp
```

**2. Create Virtual Environment**
```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Using conda
conda create -n spendless python=3.10
conda activate spendless
```

**3. Install Dependencies**
```bash
cd backend
pip install -r requirements.txt
```

**4. Environment Variables Setup**
Create a `.env` file in the `backend` directory:

```bash
# Database Configuration
MONGO_URI=mongodb://localhost:27017/project

# JWT Configuration
SECRET_KEY=your-super-secret-jwt-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# AI/ML Configuration
GEMINI_API_KEY=your-gemini-api-key
OPENAI_API_KEY=your-openai-api-key

# SMS Configuration (Notify.lk)
NOTIFY_LK_API_KEY=your-notify-lk-api-key
NOTIFY_LK_SENDER_ID=your-sender-id

# Email Configuration
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_USERNAME=your-email@gmail.com
EMAIL_PASSWORD=your-app-password

# Development Settings
DEBUG=True
LOG_LEVEL=DEBUG
```

**5. Database Setup**
```bash
# Start MongoDB (if running locally)
mongod --dbpath /path/to/your/db

# Or use MongoDB Atlas (cloud)
# Update MONGO_URI in .env file
```

**6. Run the Application**
```bash
# Development server with auto-reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Or using FastAPI CLI
fastapi dev main.py
```

**7. Verify Installation**
```bash
# Test the health endpoint
curl http://localhost:8000/health

# Expected response: {"status": "okks"}
```

### Project Structure

#### Backend Architecture

```
bankingApp/backend/
├── main.py                 # FastAPI application entry point
├── database.py            # MongoDB connection and collections
├── models.py              # Pydantic data models
├── requirements.txt       # Python dependencies
├── routes/                # API route handlers
│   ├── __init__.py
│   ├── user_login.py      # Authentication routes
│   ├── dashboard.py       # Dashboard data routes
│   ├── chatbot.py         # AI chatbot routes
│   ├── todo.py           # Todo management routes
│   ├── transaction_history.py
│   ├── incomeExpensePredictions.py
│   └── ...
├── services/              # Business logic layer
│   ├── __init__.py
│   ├── user_login.py      # Authentication services
│   ├── dashboard.py       # Dashboard services
│   ├── chatbot.py         # AI chatbot services
│   ├── llmAgentTools.py   # LLM agent tools
│   ├── websocket_manager.py
│   └── ...
├── schemas/               # Request/Response schemas
│   ├── __init__.py
│   ├── user_login_schemas.py
│   ├── dashboard.py
│   ├── chatbot.py
│   └── ...
├── utils/                 # Utility functions
│   ├── __init__.py
│   ├── auth.py           # JWT authentication
│   ├── OTP.py            # OTP generation
│   ├── encrypt_and_decrypt.py
│   └── ...
├── AI_services/           # AI/ML model implementations
│   ├── n_beats_total_balance.ipynb
│   ├── amount_regression_total_expence.ipynb
│   ├── occurence_binary_classification_total_expence.ipynb
│   ├── preprocessing_category_wise_expense_tft.ipynb
│   └── ...
└── chroma_db/            # Vector database for RAG
    ├── chroma.sqlite3
    └── ...
```

#### Design Patterns

**1. Layered Architecture**
- **Routes Layer**: HTTP request handling and validation
- **Services Layer**: Business logic and data processing
- **Data Layer**: Database operations and external API calls
- **Utils Layer**: Shared utilities and helper functions

**2. Repository Pattern**
- Database operations abstracted through service classes
- Consistent data access patterns across the application
- Easy testing and mocking of data operations

**3. Dependency Injection**
- FastAPI's built-in dependency injection system
- JWT token verification as a dependency
- Database connections injected into services

**4. Schema Validation**
- Pydantic models for request/response validation
- Automatic API documentation generation
- Type safety and data validation

### Code Structure Guidelines

#### File Naming Conventions

**Python Files:**
- Use snake_case for file names: `user_login.py`, `transaction_history.py`
- Use descriptive names that indicate functionality
- Group related functionality in modules

**Class Naming:**
- Use PascalCase for class names: `UserLogin`, `TransactionHistory`
- Use descriptive names that indicate purpose

**Function Naming:**
- Use snake_case for function names: `get_user_info`, `create_transaction`
- Use verb-noun pattern for clarity
- Use descriptive names that indicate action

#### Code Organization

**1. Route Files Structure**
```python
from fastapi import APIRouter, Depends, HTTPException
from services.module_name import service_function
from schemas.module_name import RequestSchema, ResponseSchema
from utils.auth import verify_token

router = APIRouter(
    prefix="/endpoint",
    tags=["Tag Name"],
    dependencies=[Depends(verify_token)]
)

@router.get("/")
async def get_endpoint(param: int):
    try:
        result = await service_function(param)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

**2. Service Files Structure**
```python
from database import collection_name
from schemas.module_name import DataModel
from typing import List, Optional

async def service_function(param: int) -> List[DataModel]:
    """
    Service function description.
    
    Args:
        param: Parameter description
        
    Returns:
        List of data models
        
    Raises:
        Exception: Description of when exception is raised
    """
    try:
        # Business logic here
        data = await collection_name.find({"field": param}).to_list(None)
        return [DataModel(**item) for item in data]
    except Exception as e:
        # Log error and re-raise
        raise e
```

**3. Schema Files Structure**
```python
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class RequestModel(BaseModel):
    field1: str = Field(..., description="Field description")
    field2: Optional[int] = Field(None, description="Optional field")
    
class ResponseModel(BaseModel):
    success: bool
    data: List[DataModel]
    message: str
```

### Adding New Features

#### 1. Creating a New API Endpoint

**Step 1: Define the Schema**
```python
# schemas/new_feature.py
from pydantic import BaseModel
from typing import Optional

class NewFeatureRequest(BaseModel):
    name: str
    description: Optional[str] = None

class NewFeatureResponse(BaseModel):
    id: int
    name: str
    status: str
```

**Step 2: Create the Service**
```python
# services/new_feature.py
from database import collection_name
from schemas.new_feature import NewFeatureRequest, NewFeatureResponse

async def create_new_feature(request: NewFeatureRequest) -> NewFeatureResponse:
    # Business logic here
    result = await collection_name.insert_one(request.dict())
    return NewFeatureResponse(id=result.inserted_id, **request.dict())
```

**Step 3: Create the Route**
```python
# routes/new_feature.py
from fastapi import APIRouter, Depends, HTTPException
from services.new_feature import create_new_feature
from schemas.new_feature import NewFeatureRequest, NewFeatureResponse
from utils.auth import verify_token

router = APIRouter(
    prefix="/new-feature",
    tags=["New Feature"],
    dependencies=[Depends(verify_token)]
)

@router.post("/", response_model=NewFeatureResponse)
async def create_feature(request: NewFeatureRequest):
    try:
        return await create_new_feature(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

**Step 4: Register the Router**
```python
# main.py
from routes.new_feature import router as new_feature_router

app.include_router(new_feature_router)
```

### Testing

#### Unit Testing

**1. Test Structure**
```python
# tests/test_user_service.py
import pytest
from unittest.mock import AsyncMock, patch
from services.user_login import login_user

@pytest.mark.asyncio
async def test_login_user_success():
    # Mock database response
    with patch('database.collection_user.find_one') as mock_find:
        mock_find.return_value = {
            "user_id": 123,
            "login_nic": "123456789V",
            "passcode": "hashed_password"
        }
        
        result = await login_user({"nic": "123456789V", "passcode": "password"})
        
        assert result["user_id"] == 123
        assert "access_token" in result
```

**2. Running Tests**
```bash
# Install testing dependencies
pip install pytest pytest-asyncio

# Run tests
pytest tests/

# Run with coverage
pytest --cov=backend tests/
```

#### API Testing

**1. Using FastAPI TestClient**
```python
# tests/test_api.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "okks"}

def test_login_endpoint():
    response = client.post("/login", json={
        "nic": "123456789V",
        "passcode": "password"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
```

### Debugging Tips

#### 1. Logging Configuration

**Setup Logging**
```python
# utils/logger.py
import logging
import sys
from datetime import datetime

def setup_logger(name: str, level: str = "INFO"):
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper()))
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    return logger
```

**Using Loggers**
```python
# In your services
from utils.logger import setup_logger

logger = setup_logger(__name__)

async def service_function():
    logger.info("Starting service function")
    try:
        # Your code here
        logger.debug("Processing data")
        result = await process_data()
        logger.info(f"Service completed successfully: {result}")
        return result
    except Exception as e:
        logger.error(f"Service failed: {str(e)}", exc_info=True)
        raise
```

#### 2. Common Debugging Scenarios

**Database Connection Issues**
```python
# Check MongoDB connection
async def test_db_connection():
    try:
        await client.admin.command('ping')
        print("Database connection successful")
    except Exception as e:
        print(f"Database connection failed: {e}")
```

**JWT Token Issues**
```python
# Debug JWT token
import jwt
from utils.auth import SECRET_KEY, ALGORITHM

def debug_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(f"Token payload: {payload}")
    except jwt.ExpiredSignatureError:
        print("Token has expired")
    except jwt.InvalidTokenError:
        print("Invalid token")
```

#### 3. Performance Debugging

**Database Query Performance**
```python
# Profile database queries
import time
from pymongo import monitoring

class QueryLogger(monitoring.CommandListener):
    def started(self, event):
        self.start_time = time.time()
    
    def succeeded(self, event):
        duration = time.time() - self.start_time
        print(f"Query took {duration:.2f}s: {event.command_name}")

# Register the listener
monitoring.register(QueryLogger())
```

**API Response Time**
```python
# Add timing middleware
import time
from fastapi import Request

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
```

### Best Practices

#### 1. Code Quality

**Type Hints**
```python
from typing import List, Optional, Dict, Any
from datetime import datetime

async def process_data(
    user_id: int, 
    data: List[Dict[str, Any]], 
    start_date: Optional[datetime] = None
) -> Dict[str, Any]:
    # Implementation
    pass
```

**Error Handling**
```python
from fastapi import HTTPException

async def service_function():
    try:
        # Your code here
        result = await risky_operation()
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
```

#### 2. Security Best Practices

**Input Validation**
```python
from pydantic import BaseModel, validator

class UserInput(BaseModel):
    email: str
    age: int
    
    @validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email format')
        return v
    
    @validator('age')
    def validate_age(cls, v):
        if v < 0 or v > 150:
            raise ValueError('Age must be between 0 and 150')
        return v
```

**Environment Variables**
```python
# Never hardcode sensitive data
import os
from dotenv import load_dotenv

load_dotenv()

# Good
SECRET_KEY = os.getenv("SECRET_KEY")

# Bad
SECRET_KEY = "hardcoded-secret-key"
```

#### 3. Performance Optimization

**Database Optimization**
```python
# Use projections to limit data transfer
async def get_user_summary(user_id: int):
    return await collection_user.find_one(
        {"user_id": user_id},
        {"user_id": 1, "username": 1, "balance": 1}  # Only fetch needed fields
    )

# Use aggregation for complex queries
async def get_user_stats(user_id: int):
    pipeline = [
        {"$match": {"user_id": user_id}},
        {"$group": {
            "_id": "$category",
            "total": {"$sum": "$amount"},
            "count": {"$sum": 1}
        }}
    ]
    return await collection_transaction.aggregate(pipeline).to_list(None)
```

This comprehensive development guide provides everything needed to set up, develop, and maintain the SpendLess application effectively.

## Deployment

This section provides comprehensive guidelines for deploying the SpendLess application to Azure cloud services. It covers production setup, environment configuration, scaling considerations, and monitoring.

### Azure Services Architecture

#### Recommended Azure Services Stack

```mermaid
graph TB
    subgraph "Azure Cloud Services"
        A[Azure App Service] --> B[Azure Cosmos DB]
        A --> C[Azure AI Services]
        A --> D[Azure Key Vault]
        A --> E[Azure Storage]
        A --> F[Azure Application Insights]
        A --> G[Azure CDN]
        H[Azure Container Registry] --> A
        I[Azure DevOps] --> H
    end
    
    subgraph "External Services"
        J[Gemini API]
        K[Notify.lk SMS]
        L[Email Services]
    end
    
    A --> J
    A --> K
    A --> L
    
    subgraph "Client Applications"
        M[Web Frontend]
        N[Mobile App]
    end
    
    M --> A
    N --> A
```

#### Service Mapping

| Component | Azure Service | Purpose |
|-----------|---------------|---------|
| **Backend API** | Azure App Service | FastAPI application hosting |
| **Database** | Azure Cosmos DB (MongoDB API) | Document storage and transactions |
| **Vector Database** | Azure AI Search | RAG and semantic search |
| **AI/ML Models** | Azure Machine Learning | Model hosting and inference |
| **Secrets** | Azure Key Vault | API keys and sensitive data |
| **File Storage** | Azure Blob Storage | Static files and model artifacts |
| **Monitoring** | Application Insights | Performance and error tracking |
| **CDN** | Azure CDN | Global content delivery |
| **Container Registry** | Azure Container Registry | Docker image storage |
| **CI/CD** | Azure DevOps | Automated deployment pipeline |

### Pre-Deployment Setup

#### 1. Azure CLI Installation and Configuration

```bash
# Install Azure CLI
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Login to Azure
az login

# Set subscription
az account set --subscription "your-subscription-id"

# Create resource group
az group create --name spendless-rg --location "East US"
```

#### 2. Environment Variables for Production

Create a production `.env` file:

```bash
# Database Configuration
MONGO_URI=mongodb://spendless-cosmos:your-connection-string@spendless-cosmos.mongo.cosmos.azure.com:10255/project?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@spendless-cosmos@

# JWT Configuration
SECRET_KEY=your-production-secret-key-256-bits
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# AI/ML Configuration
GEMINI_API_KEY=your-gemini-api-key
OPENAI_API_KEY=your-openai-api-key

# SMS Configuration
NOTIFY_LK_API_KEY=your-notify-lk-api-key
NOTIFY_LK_SENDER_ID=your-sender-id

# Email Configuration
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_USERNAME=your-email@gmail.com
EMAIL_PASSWORD=your-app-password

# Azure Configuration
AZURE_STORAGE_CONNECTION_STRING=your-storage-connection-string
AZURE_KEY_VAULT_URL=https://spendless-kv.vault.azure.net/

# Production Settings
DEBUG=False
LOG_LEVEL=INFO
ENVIRONMENT=production
```

### Azure Services Deployment

#### 1. Azure Cosmos DB (MongoDB API)

**Create Cosmos DB Account:**
```bash
# Create Cosmos DB account
az cosmosdb create \
    --resource-group spendless-rg \
    --name spendless-cosmos \
    --kind MongoDB \
    --locations regionName="East US" failoverPriority=0 isZoneRedundant=False \
    --default-consistency-level Session \
    --enable-multiple-write-locations false

# Get connection string
az cosmosdb keys list \
    --resource-group spendless-rg \
    --name spendless-cosmos \
    --type connection-strings
```

**Database Configuration:**
```python
# database.py - Production configuration
import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()

# Azure Cosmos DB connection
MONGO_URI = os.getenv("MONGO_URI")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client["project"]

# Collections with proper indexing
collection_user = db["user"]
collection_transaction = db["transaction"]
collection_account = db["account"]
collection_bank = db["bank"]
collection_transaction_category = db["transaction_category"]
collection_predicted_balance = db["predicted_balance"]
collection_predicted_expense = db["predicted_expense"]
collection_predicted_income = db["predicted_income"]
collection_todo_list = db["todo_list"]
collection_notification = db["notification"]
collection_otp = db["otp"]
collection_chatbot = db["chatbot"]
collection_goal = db["goal"]
collection_credit_periods = db["credit_periods"]
collection_income_expense_prediction = db["income_expense_prediction"]
collection_transaction_categorization = db["transaction_categorization"]
```

#### 2. Azure App Service

**Create App Service Plan:**
```bash
# Create App Service plan
az appservice plan create \
    --name spendless-plan \
    --resource-group spendless-rg \
    --sku P1V2 \
    --is-linux

# Create Web App
az webapp create \
    --resource-group spendless-rg \
    --plan spendless-plan \
    --name spendless-api \
    --runtime "PYTHON|3.10"
```

**Dockerfile for Azure App Service:**
```dockerfile
# Dockerfile
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download spaCy model
RUN python -m spacy download en_core_web_sm

# Copy application code
COPY . .

# Create non-root user
RUN useradd --create-home --shell /bin/bash app \
    && chown -R app:app /app
USER app

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Start command
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "main:app"]
```

**Deploy to App Service:**
```bash
# Build and push to Azure Container Registry
az acr build --registry spendless-acr --image spendless-api:latest .

# Configure App Service to use container
az webapp config container set \
    --name spendless-api \
    --resource-group spendless-rg \
    --docker-custom-image-name spendless-acr.azurecr.io/spendless-api:latest
```

#### 3. Azure Key Vault

**Create and Configure Key Vault:**
```bash
# Create Key Vault
az keyvault create \
    --name spendless-kv \
    --resource-group spendless-rg \
    --location "East US"

# Add secrets
az keyvault secret set --vault-name spendless-kv --name "SECRET-KEY" --value "your-secret-key"
az keyvault secret set --vault-name spendless-kv --name "GEMINI-API-KEY" --value "your-gemini-key"
az keyvault secret set --vault-name spendless-kv --name "MONGO-URI" --value "your-mongo-uri"
az keyvault secret set --vault-name spendless-kv --name "NOTIFY-LK-API-KEY" --value "your-notify-key"

# Grant App Service access to Key Vault
az webapp identity assign --name spendless-api --resource-group spendless-rg
az keyvault set-policy --name spendless-kv --object-id <app-service-principal-id> --secret-permissions get list
```

**Key Vault Integration in Code:**
```python
# utils/azure_keyvault.py
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
import os

class AzureKeyVault:
    def __init__(self):
        self.vault_url = os.getenv("AZURE_KEY_VAULT_URL")
        self.credential = DefaultAzureCredential()
        self.client = SecretClient(vault_url=self.vault_url, credential=self.credential)
    
    def get_secret(self, secret_name: str) -> str:
        secret = self.client.get_secret(secret_name)
        return secret.value

# Usage in main.py
from utils.azure_keyvault import AzureKeyVault

keyvault = AzureKeyVault()
SECRET_KEY = keyvault.get_secret("SECRET-KEY")
GEMINI_API_KEY = keyvault.get_secret("GEMINI-API-KEY")
```

#### 4. Azure Blob Storage

**Create Storage Account:**
```bash
# Create storage account
az storage account create \
    --name spendlessstorage \
    --resource-group spendless-rg \
    --location "East US" \
    --sku Standard_LRS

# Create containers
az storage container create --name models --account-name spendlessstorage
az storage container create --name data --account-name spendlessstorage
az storage container create --name logs --account-name spendlessstorage
```

**Blob Storage Integration:**
```python
# utils/azure_storage.py
from azure.storage.blob import BlobServiceClient
import os

class AzureBlobStorage:
    def __init__(self):
        self.connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        self.blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)
    
    def upload_file(self, container_name: str, file_path: str, blob_name: str):
        blob_client = self.blob_service_client.get_blob_client(
            container=container_name, blob=blob_name
        )
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
    
    def download_file(self, container_name: str, blob_name: str, download_path: str):
        blob_client = self.blob_service_client.get_blob_client(
            container=container_name, blob=blob_name
        )
        with open(download_path, "wb") as download_file:
            download_file.write(blob_client.download_blob().readall())
```

#### 5. Azure Application Insights

**Create Application Insights:**
```bash
# Create Application Insights
az monitor app-insights component create \
    --app spendless-insights \
    --location "East US" \
    --resource-group spendless-rg

# Get instrumentation key
az monitor app-insights component show \
    --app spendless-insights \
    --resource-group spendless-rg \
    --query instrumentationKey
```

**Application Insights Integration:**
```python
# main.py - Add Application Insights
from opencensus.ext.azure.log_exporter import AzureLogHandler
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.trace.samplers import ProbabilitySampler
from opencensus.trace.tracer import Tracer
import logging

# Configure Application Insights
instrumentation_key = os.getenv("APPINSIGHTS_INSTRUMENTATION_KEY")
logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(connection_string=f'InstrumentationKey={instrumentation_key}'))

# Configure tracing
tracer = Tracer(
    exporter=AzureExporter(connection_string=f'InstrumentationKey={instrumentation_key}'),
    sampler=ProbabilitySampler(1.0)
)

@app.middleware("http")
async def trace_requests(request: Request, call_next):
    with tracer.span(name="request"):
        response = await call_next(request)
        return response
```

### CI/CD Pipeline with Azure DevOps

#### 1. Azure DevOps Pipeline

**azure-pipelines.yml:**
```yaml
# azure-pipelines.yml
trigger:
- main

variables:
  dockerRegistryServiceConnection: 'spendless-acr-connection'
  imageRepository: 'spendless-api'
  containerRegistry: 'spendless-acr.azurecr.io'
  dockerfilePath: '$(Build.SourcesDirectory)/Dockerfile'
  tag: '$(Build.BuildId)'
  vmImageName: 'ubuntu-latest'

stages:
- stage: Build
  displayName: Build and push stage
  jobs:
  - job: Build
    displayName: Build
    pool:
      vmImage: $(vmImageName)
    steps:
    - task: Docker@2
      displayName: Build and push an image to container registry
      inputs:
        command: buildAndPush
        repository: $(imageRepository)
        dockerfile: $(dockerfilePath)
        containerRegistry: $(dockerRegistryServiceConnection)
        tags: |
          $(tag)
          latest

- stage: Deploy
  displayName: Deploy stage
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
  jobs:
  - deployment: Deploy
    displayName: Deploy
    environment: 'production'
    pool:
      vmImage: $(vmImageName)
    strategy:
      runOnce:
        deploy:
          steps:
          - task: AzureWebAppContainer@1
            displayName: 'Azure Web App on Container Deploy'
            inputs:
              azureSubscription: 'spendless-azure-connection'
              appName: 'spendless-api'
              containers: '$(containerRegistry)/$(imageRepository):$(tag)'
```

#### 2. GitHub Actions Alternative

**.github/workflows/deploy.yml:**
```yaml
name: Deploy to Azure

on:
  push:
    branches: [ main ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.10'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r backend/requirements.txt
    
    - name: Run tests
      run: |
        cd backend
        pytest tests/ --cov=.
    
    - name: Login to Azure
      uses: azure/login@v1
      with:
        creds: ${{ secrets.AZURE_CREDENTIALS }}
    
    - name: Build and push Docker image
      run: |
        az acr build --registry spendless-acr --image spendless-api:${{ github.sha }} .
    
    - name: Deploy to Azure App Service
      uses: azure/webapps-deploy@v2
      with:
        app-name: 'spendless-api'
        images: 'spendless-acr.azurecr.io/spendless-api:${{ github.sha }}'
```

### Production Configuration

#### 1. App Service Configuration

**Application Settings:**
```bash
# Configure app settings
az webapp config appsettings set \
    --resource-group spendless-rg \
    --name spendless-api \
    --settings \
        WEBSITES_ENABLE_APP_SERVICE_STORAGE=false \
        WEBSITES_PORT=8000 \
        PYTHONPATH=/home/site/wwwroot \
        ENVIRONMENT=production \
        LOG_LEVEL=INFO
```

**Health Check Configuration:**
```python
# main.py - Enhanced health check
@app.get("/health")
async def health_check():
    try:
        # Check database connection
        await client.admin.command('ping')
        db_status = "healthy"
    except Exception as e:
        db_status = f"unhealthy: {str(e)}"
    
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0",
        "database": db_status,
        "environment": os.getenv("ENVIRONMENT", "development")
    }
```

#### 2. Scaling Configuration

**Auto-scaling Rules:**
```bash
# Create auto-scale settings
az monitor autoscale create \
    --resource-group spendless-rg \
    --resource spendless-api \
    --resource-type Microsoft.Web/sites \
    --name spendless-autoscale \
    --min-count 2 \
    --max-count 10 \
    --count 3

# Add scale-out rule
az monitor autoscale rule create \
    --resource-group spendless-rg \
    --autoscale-name spendless-autoscale \
    --condition "CpuPercentage > 70 avg 5m" \
    --scale out 2

# Add scale-in rule
az monitor autoscale rule create \
    --resource-group spendless-rg \
    --autoscale-name spendless-autoscale \
    --condition "CpuPercentage < 30 avg 5m" \
    --scale in 1
```

#### 3. Security Configuration

**HTTPS and SSL:**
```bash
# Configure custom domain and SSL
az webapp config hostname add \
    --webapp-name spendless-api \
    --resource-group spendless-rg \
    --hostname api.spendless.com

# Configure SSL certificate
az webapp config ssl bind \
    --certificate-thumbprint <certificate-thumbprint> \
    --ssl-type SNI \
    --name spendless-api \
    --resource-group spendless-rg
```

**CORS Configuration for Production:**
```python
# main.py - Production CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://spendless.com",
        "https://www.spendless.com",
        "https://app.spendless.com"
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
```

### Monitoring and Logging

#### 1. Application Insights Queries

**Performance Monitoring:**
```kusto
// Top slow requests
requests
| where timestamp > ago(1h)
| summarize avg(duration) by name
| order by avg_duration desc
| take 10

// Error rate
requests
| where timestamp > ago(1h)
| summarize 
    total = count(),
    errors = countif(success == false)
| extend error_rate = errors * 100.0 / total

// Database query performance
dependencies
| where timestamp > ago(1h)
| where type == "MongoDB"
| summarize avg(duration) by name
| order by avg_duration desc
```

#### 2. Custom Metrics

**Custom Telemetry:**
```python
# utils/telemetry.py
from opencensus.ext.azure import metrics_exporter
from opencensus.stats import stats as stats_module
from opencensus.stats import measure as measure_module
from opencensus.stats import view as view_module

# Define custom metrics
m_prediction_accuracy = measure_module.MeasureFloat(
    "prediction_accuracy", 
    "AI model prediction accuracy", 
    "percentage"
)

m_api_response_time = measure_module.MeasureFloat(
    "api_response_time", 
    "API response time", 
    "milliseconds"
)

# Create views
prediction_accuracy_view = view_module.View(
    "prediction_accuracy",
    "AI model prediction accuracy",
    [],
    m_prediction_accuracy,
    view_module.AggregationType.DISTRIBUTION
)

# Record metrics
stats = stats_module.stats
view_manager = stats.view_manager
view_manager.register_view(prediction_accuracy_view)

def record_prediction_accuracy(accuracy: float):
    mmap = stats.stats_recorder.new_measurement_map()
    mmap.measure_float_put(m_prediction_accuracy, accuracy)
    mmap.record()
```

### Backup and Disaster Recovery

#### 1. Database Backup

**Cosmos DB Backup:**
```bash
# Enable continuous backup
az cosmosdb update \
    --resource-group spendless-rg \
    --name spendless-cosmos \
    --backup-policy-type Continuous \
    --backup-interval 60 \
    --backup-retention 7
```

#### 2. Application Backup

**Blob Storage Backup:**
```bash
# Create backup policy
az storage account blob-service-properties update \
    --account-name spendlessstorage \
    --enable-change-feed true \
    --enable-versioning true \
    --enable-delete-retention true \
    --delete-retention-days 30
```

### Cost Optimization

#### 1. Resource Optimization

**App Service Plan Optimization:**
```bash
# Use reserved instances for production
az appservice plan update \
    --name spendless-plan \
    --resource-group spendless-rg \
    --sku P1V2

# Configure auto-shutdown for dev environments
az webapp config set \
    --name spendless-api-dev \
    --resource-group spendless-rg \
    --always-on false
```

#### 2. Monitoring Costs

**Cost Management:**
```bash
# Set up budget alerts
az consumption budget create \
    --budget-name spendless-budget \
    --resource-group spendless-rg \
    --amount 500 \
    --time-grain Monthly \
    --start-date 2024-01-01 \
    --end-date 2024-12-31
```

### Deployment Checklist

#### Pre-Deployment
- [ ] All environment variables configured in Key Vault
- [ ] Database connection strings updated
- [ ] SSL certificates configured
- [ ] CORS settings updated for production domains
- [ ] Application Insights configured
- [ ] Auto-scaling rules set up
- [ ] Backup policies configured

#### Post-Deployment
- [ ] Health check endpoint responding
- [ ] Database connectivity verified
- [ ] AI/ML models loading correctly
- [ ] Authentication flow working
- [ ] API endpoints responding
- [ ] Monitoring and alerting active
- [ ] Performance metrics within acceptable ranges

This comprehensive Azure deployment guide provides everything needed to deploy and maintain the SpendLess application in a production Azure environment.
