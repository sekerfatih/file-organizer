import os
import tempfile
import shutil
from file_organizer import organize_files

def test_file_organization():
    """Test that files get organized into correct folders"""
    
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"Testing in: {temp_dir}")
        
        # Create test files
        test_files = [
            "photo.jpg",
            "video.mp4", 
            "document.pdf",
            "song.mp3"  # This should go to "Files" since mp3 isn't in your categories
        ]
        
        # Actually create the test files
        for filename in test_files:
            with open(f"{temp_dir}/{filename}", 'w') as f:
                f.write("test content")
        
        print("Created test files:", test_files)
        
        # Run your organizer
        organize_files(temp_dir)
        
        # Check if the right folders were created
        expected_folders = ["Images", "Videos", "Files"]
        for folder in expected_folders:
            folder_path = os.path.join(temp_dir, folder)
            if os.path.exists(folder_path):
                print(f"✅ {folder} folder created")
            else:
                print(f"❌ {folder} folder missing")
        
        # Check if files are in the right places
        if os.path.exists(f"{temp_dir}/Images/photo.jpg"):
            print("✅ photo.jpg moved to Images")
        else:
            print("❌ photo.jpg not in Images")
            
        print("Test completed!")

if __name__ == "__main__":
    test_file_organization()