

if($(Get-Package git) -eq $null) 
{
    echo "Please install git to proeceed"
    
    exit
}

$tempPath = "$($env:USERPROFILE)\AppData\Local\Temp\temp_creaject_templ"
$targetPath = "$($env:APPDATA)\creaject"

mkdir $tempPath
mkdir $targetPath

cd $($tempPath)
git clone -q https://github.com/tholuce/creaject-templates
cd .\creaject-templates

Copy-Item  ".\templates\" -Destination $targetPath -Recurse
cd $targetPath


Remove-Item -Path $tempPath -Recurse -Force