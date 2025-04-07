class Modelmake < Formula
  desc "3D Model Conversion, Scaling, and Optimization Tool"
  homepage "https://github.com/sudo-self/makemodel-homebrew"
  url "https://github.com/sudo-self/makemodel-homebrew/raw/main/modelmake.tar.gz"
  sha256 "26d564a629d69dfdd4c4d22c61ed3df160e94a46b483350244e8553917370f7e"  # Replace this with the actual sha256 of the tarball
  license "MIT"  # Add the correct license if it's different

  depends_on "python@3.9"

  def install
    # Install the necessary files to the correct locations
    bin.install Dir["*"]
  end

  test do
    # Ensure the command works as expected
    system "#{bin}/modelmake", "--help"
  end
end




