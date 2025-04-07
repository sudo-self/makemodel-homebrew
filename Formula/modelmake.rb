class Modelmake < Formula
  desc "3D Model Conversion, Scaling, and Optimization Tool"
  homepage "https://github.com/sudo-self/makemodel-homebrew"
  url "https://github.com/sudo-self/makemodel-homebrew/blob/main/modelmake.tar.gz", using: :curl
  sha256 "26d564a629d69dfdd4c4d22c61ed3df160e94a46b483350244e8553917370f7e"

  depends_on "python@3.9"

  def install
 
    bin.install Dir["*"]
  end

  test do
    
    system "#{bin}/modelmake", "--help"
  end
end
