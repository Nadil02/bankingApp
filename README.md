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
- Prerequisites
- Environment setup
- Dependencies installation
- Database setup
- Initial configuration

## Configuration
- Environment variables
- API keys setup
- Database configuration
- AI model configuration

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