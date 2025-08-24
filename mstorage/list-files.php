<?php
header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *');

$folderPath = __DIR__ . '/files/';

if (!is_dir($folderPath)) {
    echo json_encode([]);
    exit;
}

$files = [];
$items = scandir($folderPath);

foreach ($items as $item) {
    $filePath = $folderPath . $item;
    if ($item !== '.' && $item !== '..' && is_file($filePath)) {
        $files[] = [
            'name' => $item,
            'size' => filesize($filePath),
            'path' => 'files/' . rawurlencode($item)
        ];
    }
}

usort($files, fn($a, $b) => strcasecmp($a['name'], $b['name']));

echo json_encode($files, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);