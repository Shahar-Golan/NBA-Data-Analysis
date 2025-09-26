# Enhanced NBA Data Analysis GUI

## New Features

### 🎨 **Modern Visual Design**
- **Professional Dark Theme**: NBA-inspired color scheme with dark blue background, red and blue accents
- **Card-based Layout**: Clean, modern cards for better content organization
- **Typography**: Improved fonts and text hierarchy for better readability

### 🖼️ **Image Integration**
- **NBA Logo Background**: Subtle NBA logo watermark in the header
- **Hero Images**: 
  - Air Jordan image for Player Analytics section
  - LeBron's block image for Machine Learning section
  - Kobe & Shaq image in the analytics header
- **Circular Image Processing**: All player images are automatically cropped to circular shapes

### 🎯 **Interactive Elements**
- **Hover Effects**: Buttons change color when hovered over for better user feedback
- **Modern Buttons**: Flat design with NBA-themed colors and smooth transitions
- **Responsive Layout**: Better use of screen space with responsive design

### 📊 **Enhanced Analytics Visualization**
- **Improved Charts**: Modern dark-themed charts with NBA color scheme
- **Value Labels**: Bars now show exact values on top for better readability
- **Better Grid System**: Subtle grid lines for easier data reading
- **Professional Styling**: Consistent with the overall app theme

### 🗂️ **Improved User Experience**
- **Clear Navigation**: Better back button placement and navigation flow
- **Contextual Information**: Season and analysis type clearly displayed
- **Better Error Handling**: More user-friendly error messages
- **Organized Layout**: Logical grouping of related functionality

## Technical Improvements

### Dependencies Added
- **Pillow (PIL)**: For image processing and manipulation
- **Enhanced Matplotlib**: Better chart styling and theming

### File Structure
```
GUI/
├── main_file.py              # Enhanced main application with modern styling
├── season_selection.py       # Modern season selection with hero images
├── options_screen.py         # Enhanced analytics screen with better UX
├── *_original.py            # Backup of original files
└── ...
```

### Color Scheme
- **Primary**: #c9302c (NBA Red)
- **Secondary**: #0f3460 (NBA Blue)  
- **Background**: #1a1a2e (Dark Blue)
- **Surface**: #16213e (Card Background)
- **Text Primary**: #ffffff (White)
- **Text Secondary**: #b0b0b0 (Gray)
- **Accent**: #ffd700 (Gold)

## Running the Enhanced Application

1. Install dependencies:
   ```
   pip install Pillow matplotlib pandas numpy tkinter
   ```

2. Run the application:
   ```
   python main_file.py
   ```

## Asset Integration

The application now uses the following images from the `assests` folder:
- `nba-logo-design.webp` - Background watermark
- `Air Jordan.jpg` - Player Analytics hero image
- `Lebron's block.jpg` - Machine Learning hero image
- `Kobe & Shaq.jpg` - Analytics header image

All images are processed to fit the design and maintain consistent styling.