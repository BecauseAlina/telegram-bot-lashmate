# LuxeLash - Beauty Salon Booking System

## Overview

LuxeLash is a comprehensive beauty salon booking system specifically designed for eyelash extension services. The application provides a seamless booking experience for customers and a powerful admin dashboard for salon management. Built as a full-stack web application, it handles service selection, appointment scheduling, customer management, and business analytics.

The system features a modern, responsive frontend with a beauty-focused design theme using rose gold and cream colors, providing an elegant user experience that matches the luxury beauty industry aesthetic.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Framework**: React 18 with TypeScript for type safety and modern component development
- **Routing**: Wouter for lightweight client-side routing with two main routes (home and admin)
- **Styling**: Tailwind CSS with custom beauty-themed color palette and Shadcn/ui component library
- **State Management**: TanStack Query (React Query) for server state management and caching
- **Forms**: React Hook Form with Zod validation for robust form handling
- **Build Tool**: Vite for fast development and optimized production builds

### Backend Architecture
- **Runtime**: Node.js with Express.js framework
- **Language**: TypeScript with ES modules for modern JavaScript features
- **API Design**: RESTful API architecture with structured endpoints for services, appointments, and availability
- **Error Handling**: Centralized error handling middleware with proper HTTP status codes
- **Development**: Hot reload development server with integrated frontend/backend development

### Database Layer
- **ORM**: Drizzle ORM for type-safe database operations
- **Database**: PostgreSQL with Neon Database serverless hosting
- **Schema Management**: Drizzle Kit for migrations and schema management
- **Storage Pattern**: Repository pattern with in-memory storage implementation for development

### Data Models
The system uses three core entities:
- **Services**: Eyelash extension services with pricing, duration, and descriptions
- **Customers**: Client information including contact details and booking history
- **Appointments**: Booking records linking customers to services with scheduling details

### Authentication & Session Management
- **Session Storage**: PostgreSQL-based session storage using connect-pg-simple
- **Security**: Environment-based configuration with secure session handling

### UI/UX Design System
- **Component Library**: Radix UI primitives with custom styling
- **Theme**: Custom beauty-focused design system with rose gold primary colors
- **Typography**: Inter and Open Sans font families for modern, readable design
- **Responsive Design**: Mobile-first approach with Tailwind's responsive utilities

### Development Environment
- **Replit Integration**: Custom Vite plugins for Replit development environment
- **TypeScript Configuration**: Strict type checking with path mapping for clean imports
- **Code Quality**: ESLint and TypeScript compiler for code quality assurance

## External Dependencies

### Database Services
- **Neon Database**: Serverless PostgreSQL hosting for scalable data storage
- **Connection**: @neondatabase/serverless for optimized serverless database connections

### UI Framework & Components
- **Radix UI**: Complete suite of accessible, unstyled UI primitives for building the component library
- **Lucide React**: Modern icon library for consistent iconography throughout the application
- **Tailwind CSS**: Utility-first CSS framework for responsive design and custom theming

### Development & Build Tools
- **Vite**: Modern build tool with hot module replacement and optimized bundling
- **TypeScript**: Static type checking for enhanced developer experience and code reliability
- **PostCSS**: CSS processing with Tailwind CSS and Autoprefixer plugins

### Form & Validation Libraries
- **React Hook Form**: Performant forms library with minimal re-renders
- **Zod**: TypeScript-first schema validation library
- **@hookform/resolvers**: Integration between React Hook Form and Zod validation

### State Management & API
- **TanStack Query**: Powerful data synchronization for server state management
- **Date-fns**: Modern date utility library for handling appointment scheduling

### Session & Security
- **Express Session**: Session middleware for Express.js
- **Connect PG Simple**: PostgreSQL session store for persistent session management

### Development Environment
- **@replit/vite-plugin-runtime-error-modal**: Enhanced error reporting in Replit environment
- **@replit/vite-plugin-cartographer**: Development tooling for Replit integration
- **tsx**: TypeScript execution for Node.js development server